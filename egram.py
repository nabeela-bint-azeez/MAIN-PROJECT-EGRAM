import os
from flask import *
from src.dbconnectionnew import *
from werkzeug.utils import secure_filename
#
import datetime
import random
from flask import Flask, abort, send_file
from flask_script import Manager
from flask_cors import CORS
import os
import requests
import ipfshttpclient


app=Flask(__name__)
app.secret_key="dfghjk"


#
systempath=r"D:\projectBackupModified23052023\eg\src\static\\"
CORS(app)
app.config.from_pyfile('config.py')
import json

from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = r"D:\projectBackup\egro\src\node_modules\.bin\build\contracts\StructDemo.json"
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xDE83cB3Ba99374D6300B255d561E0c6CE535c40C'
#
manager = Manager(app)

def download(url):
    h = {"Accept-Encoding": "identity"}
    r = requests.get(url, stream=True, verify=False, headers=h)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        #log.exception("IPFS Server Error! url:{0}, exception:{1}".format(url, str(e)))
        return "IPFS Server Error! \n", 503

    if "content-type" in r.headers:
        return send_file(r.raw, r.headers["content-type"])
    else:
        return send_file(r.raw)


# @app.route("/<path:path>")
@app.route("/down/<path:path>")
def down(path):
    try:
        p = os.path.splitext(path)
        hash = str(p[0])

        if not hash or not hash.startswith('Qm'):
            return "<Invalid Path>", 404

        #log.info("hash:{0}".format(hash), {'app': 'dfile-down-req'})

        url = app.config['IPFS_FILE_URL'] + hash

        return download(url)
    except Exception as e:
        #log.exception("Download Error! path:{0}, exception:{1}".format(path, str(e)))
        return "Download Error! \n", 503






@app.route('/')
def log():
    return render_template("loginnew.html")

@app.route('/login',methods=['post'])
def login():
   username=request.form['textfield']
   password=request.form['textfield2']
   qry="select*from login where username=%s and password=%s"
   val=(username,password)
   res=selectone(qry,val)
   if res is None:
       return''' <script>alert("fill username and password");
       window.location="/"</script>'''
   elif  res['type']=='admin':
        session['lid']=res['lid']
        return redirect('adminhome')
   elif res['type'] == 'user':
       session['lid'] = res['lid']
       return redirect('userhome')
       # return redirect('userviewnotification')
   elif res['type'] == 'staff':
       session['lid'] = res['lid']
       return redirect('staffhome')
   else:
       return ''' <script>alert("incorrect username or password");
              window.location="/"</script>'''



   #admin route

@app.route('/adminhome')
def adminhome():
    return render_template("aindex.html")


@app.route('/addnotification')
def add_notification():
    return render_template("admin/add notification.html")


@app.route('/addnotification1',methods=['post'])
def add_notification1():
    content=request.form['textfield']
    q="INSERT INTO `notification` VALUES(NULL,%s,CURDATE())"
    iud(q,content)
    return ''' <script>alert("added");
               window.location="/adminhome"</script>'''

@app.route('/addrequirements')
def add_requirements():
    qry="select * from services"
    res=selectall(qry)
    return render_template("admin/add requirements.html",val=res)

@app.route('/addservice',methods=['post'])
def addservice():
    return render_template("admin/add service.html")


@app.route('/addtax',methods=['post'])
def addtax():
    qry="select * from user "
    res=selectall(qry)
    return render_template("admin/add tax.html",v=res)

@app.route('/addstaff',methods=['POST'])
def addstaff():
    return render_template("admin/addstaff.html")


@app.route('/managestaff')
def managestaff():
    qry="select*from staff"
    val=selectall(qry)
    return render_template("admin/manage staff.html",data=val)


@app.route('/deletestaff')
def deletestaff():
    id=request.args.get('id')
    qry="delete from staff where lid=%s"
    iud(qry,id)
    qry1= "delete from login where lid=%s"
    iud(qry1, id)
    return ''' <script>alert("de;leted");
               window.location="/managestaff"</script>'''




@app.route('/managetax')
def managetax():
    qry = "select * from tax_info join user on tax_info.user_id=user.lid"
    val = selectall(qry)
    return render_template("admin/manage tax.html", data=val)



@app.route('/updateservice')
def updateservice():
    qry = "select*from services"
    val = selectall(qry)
    return render_template("admin/update service.html", data=val)


@app.route('/updatestatus')
def updatestatus():
    q="SELECT `user`.`name`,`services`.`service_name`,`service_request`.* FROM `services` JOIN `service_request` ON `services`.`service_id`=`service_request`.`service_id` JOIN `user` ON `user`.`lid`=`service_request`.`user_id`"
    res=selectall(q)
    return render_template("admin/update status.html",val=res)

@app.route('/acceptrequest')
def acceptrequest():
    id=request.args.get('id')
    q="UPDATE `service_request` SET `status`='accepted' WHERE `request_id`=%s"
    iud(q,str(id))


    return ''' <script>alert("accepted");
               window.location="/updatestatus"</script>'''


@app.route('/rejectrequest')
def rejectrequest():
    id=request.args.get('id')
    q="UPDATE `service_request` SET `status`='rejected' WHERE `request_id`=%s"
    iud(q,str(id))


    return ''' <script>alert("Rejected");
               window.location="/updatestatus"</script>'''


@app.route('/viewcomplaints')
def viewcomplaints():
    qry = "SELECT `user`.`name`,`complaints`.* FROM `complaints` JOIN `user` ON `user`.`lid`=`complaints`.`user_id`"
    val = selectall(qry)
    return render_template("admin/view complaint.html", data=val)




#staff route

@app.route('/staffhome')
def staffhome():
    return render_template("sindex.html")

@app.route('/upldcertficate',methods=['get','post'])
def upldcertficate():
    rid = request.args.get('id')

    if request.method=="POST":

        f = request.files['file']
        f.save(systempath + "a.pdf")

        import hashlib

        res = selectone("SELECT * FROM `certificate` WHERE `rid`=%s",rid)
        if res is None:

            filename = r'D:\projectBackup\egro\src\static\a.pdf'
            sha256_hash = hashlib.sha256()
            has = ""
            with open(filename, "rb") as f:
                # Read and update hash string value in blocks of 4K
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
                has = sha256_hash.hexdigest()
                print(sha256_hash.hexdigest())
            # db = Db()

            client = ipfshttpclient.connect(app.config['IPFS_CONNECT_URL'])
            res = client.add(systempath + "a.pdf")

            iud("INSERT INTO `certificate`(`rid`,`certificate`,`date`) VALUES(%s,%s,CURDATE())",(str(rid),str(res['Hash'])))

            # log.info("upload res: {}".format(res), {'app': 'dfile-up-res'})
            url = app.config['DOMAIN'] + '/' + str(res['Hash'])
            print(url, "kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            with open(compiled_contract_path) as file:
                contract_json = json.load(file)  # load contract info as JSON
                contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
            contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
            blocknumber = web3.eth.get_block_number()
            message2 = contract.functions.addrecords(blocknumber + 1,
                                                     int(rid),
                                                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                                     str(res['Hash'])).transact()
            iud('UPDATE `service_request` SET `status`=%s WHERE `request_id`=%s',('uploaded',rid))

            return '<script>alert("Added");window.location="/verifypay"</script>'
        else:
            return '<script>alert("Aleready uploaded");window.location="/verifypay"</script>'



    else:

        return render_template("staff/upload certificate.html")

@app.route('/verify')
def verify():
    qry = "SELECT `service_request`.*,`services`.`service_name`,`services`.`amount`,`user`.`name`,`user`.`lid` FROM `service_request` JOIN `services`ON `service_request`.`service_id`=`services`.`service_id` JOIN `user`ON `user`.`lid`=`service_request`.`user_id`"
    val = selectall(qry)
    print(val)
    return render_template("staff/verify application&update status.html", data=val)


@app.route('/seemore')
def seemore():
    print(request.form)
    id=request.args.get('id')
    session['EEE_id']=id
    un=request.args.get('un')
    session['UID']=un


    sname=request.args.get('sn')
    if sname=="Birth Certificate":
        return redirect('/viewbirth')
    elif sname=="Death Certificate":
        return redirect('/viewdeath')
    elif sname=="Marriage Certificate":
        return redirect('/viewmarriage')
    else:
        return redirect('/viewownership')




@app.route('/verifydoc')
def verifydoc():
    id=request.args.get('id')
    print(id,"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    sid=request.args.get('sid')
    print(sid,"serrrrrrrrrrrrrrrrrrrrrrrrrr")
    q="SELECT * FROM `requirements` WHERE `service_id`=%s"
    res=selectall2(q,sid)
    print(res)

    doc=["'0'"]

    for i in res:
        doc.append("'"+i['documents']+"'")
        print(doc,"docccccccccc")
    s=",".join(doc)
    print(s,"sssssssss")
    qry = "SELECT * FROM `documents` WHERE `uid`=%s AND `type` IN("+s+")"
    r = selectall2(qry,id)
    print(r)

    return render_template("staff/verify documents.html",val=res,v=r)

@app.route('/verifypay')
def verifypay():
    q="SELECT  service_request.status as st , `payment` .*, `services`.`service_name`,`user`.`name`,`service_request`.`request_id` FROM `user` JOIN `payment` ON `payment`.`user_id`=`user`.`lid` JOIN `service_request` ON `service_request`.`request_id`=`payment`.`request_id` JOIN `services` ON `services`.`service_id`=`service_request`.`service_id`"
    res=selectall(q)
    print(res)
    return render_template("staff/view&verify payment.html",val=res)



@app.route('/userviewnotification')
def userviewnotification():
    return render_template("user/view notification.html")



@app.route('/viewservicestaff')
def viewservicestaff():
    qry = "select*from services"
    val = selectall(qry)
    return render_template("staff/view services.html", data=val)



#user route

@app.route('/userhome')
def userhome():
    q="SELECT * FROM `notification`"
    res=selectall(q)

    q1 = "select count(notification_id) as cnt from notification where date=curdate()"
    res1 = selectonee(q1)

    return render_template("uindex.html",st="not",val=res,val2=res1['cnt'])

@app.route('/reg')
def reg():
    return render_template("user/registration.html")


@app.route('/addcomplaint')
def addcomplaint():
    return render_template("user/add complaint.html")

@app.route('/birth')
def birth():
    return render_template("user/birth.html")

@app.route('/death')
def death():
    return render_template("user/death.html")

@app.route('/marriage')
def marriage():
    return render_template("user/marriage.html")

@app.route('/ownership')
def ownership():
    return render_template("user/ownership.html")

@app.route('/taxhistory')
def taxhistory():
    q="SELECT * FROM `tax_info` JOIN `tax_payment` ON `tax_info`.`tax_id`=`tax_payment`.`tax_id` WHERE `tax_payment`.`user_id`=%s"
    res=selectall2(q,session['lid'])
    return render_template("user/tax history.html",val=res)

@app.route('/upldocs')
def upldocs():
    qry = "SELECT * FROM requirements WHERE service_id=%s AND `documents` NOT IN(SELECT `type` FROM `documents` WHERE `uid`=%s)"
    val = selectall2(qry,(session['serid'],session['lid']))
    if len(val)>0:
        return render_template("user/upload documents.html",data=val)
    else:
        return ''' <script>alert("applied successfully");
              window.location="/user_pay_proceed1"</script>'''


@app.route('/insert_document',methods=['post'])
def insert_document():
    f=request.files['file']
    ty=request.form['select']
    fn=secure_filename(f.filename)
    f.save("static/document/"+fn)



    import hashlib

    filename = r'static/document/'+fn
    sha256_hash = hashlib.sha256()
    has = ""
    with open(filename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        has = sha256_hash.hexdigest()
        print(sha256_hash.hexdigest())
    # db = Db()

    client = ipfshttpclient.connect(app.config['IPFS_CONNECT_URL'])
    res = client.add(filename)
    #


    qry="INSERT INTO `documents` VALUES(NULL,%s,%s,%s,'pending')"
    val=(str(res['Hash']),session['lid'],ty)
    iud(qry,val)
    qry = "SELECT * FROM requirements WHERE service_id=%s AND `documents` NOT IN(SELECT `type` FROM `documents` WHERE `uid`=%s)"
    val = selectall2(qry,(session['serid'],session['lid']))
    if len(val)>0:
        return render_template("user/upload documents.html",data=val)
    else:
        return ''' <script>alert("applied successfully");
              window.location="/user_pay_proceed1"</script>'''



@app.route('/apply')
def apply():
    id=request.args.get('id')
    session['serid']=id
    amm=request.args.get('amtt')
    session['samt']=amm
    sname=request.args.get('ser')

    if sname=="Birth Certificate":
        return redirect('/birth')
    elif sname=="Death Certificate":
        return redirect('/death')
    elif sname=="Marriage Certificate":
        return redirect('/marriage')
    elif sname=="Ownership Certificate":
        q="SELECT  * FROM `tax_payment` WHERE `year`=YEAR(CURDATE())-1"
        res=selectonee(q)
        print(res)
        if res is None:
            return '''<script>alert("please pay the pending tax ");window.location='/viewservice'</script>'''
        else:

            return redirect('/ownership')






@app.route('/viewservice')
def viewservice():
    qry = "select*from services"
    val = selectall(qry)
    return render_template("user/view service.html" ,data=val)


@app.route('/viewstatus')
def viewstatus():
    qry = "SELECT * FROM `service_request` JOIN `services` ON `services`.`service_id`=`service_request`.`service_id` LEFT JOIN `certificate` ON `certificate`.`rid`=`service_request`.`request_id` WHERE `service_request`.`user_id`=%s"
    val = selectall2(qry,session['lid'])
    return render_template("user/view status.html", data=val)


@app.route('/viewtax')
def viewtax():
    qry = "SELECT * FROM `tax_info` WHERE `user_id`=%s"
    val = selectall2(qry,session['lid'])
    return render_template("user/view tax.html", data=val)



@app.route('/viewreply')
def viewreply():
    qry = "select*from complaints where user_id=%s"
    val = selectall2(qry,session['lid'])
    return render_template("user/view reply.html", data=val)


@app.route('/register',methods=['post'])
def register():
    name=request.form['textfield']
    gender=request.form['radiobutton']
    dob=request.form['textfield2']
    age = request.form['textfield23']

    photo=request.files['file']
    finame=secure_filename(photo.filename)
    photo.save(os.path.join('static/image',finame))

    signature=request.files['file2']
    filname1 = secure_filename(signature.filename)
    photo.save(os.path.join('static/image', filname1))

    houseno=request.form['textfield3']
    housename=request.form['textfield222']
    locality=request.form['textfield22']
    postoffice=request.form['textfield223']
    pin=request.form['textfield224']
    district = request.form['textfield2242']
    taluk = request.form['textfield2243']
    village = request.form['textfield2244']
    fname=request.form['textfield22422']
    mnane=request.form['textfield22423']
    mstatus=request.form['textfield22424']

    phone = request.form['textfield22425']
    email = request.form['textfield22426']
    licence = request.form['textfield22427']
    passport = request.form['textfield22428']
    sslc = request.form['textfield22429']
    ration = request.form['textfield224210']
    election = request.form['textfield224211']
    adhar = request.form['textfield224212']
    usename = request.form['username']
    password = request.form['password']

    qry="insert into login values(null,%s,%s,'user')"
    val=(usename,password)
    id=iud(qry,val)
    q="INSERT INTO `user` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    va=(str(id),name,gender,dob,age,finame,filname1,houseno,housename,locality,postoffice,pin,district,taluk,village,fname,mnane,mstatus,phone,email,licence,passport,sslc,ration,election,adhar)

    iud(q,va)
    return ''' <script>alert("success");window.location="/"</script>'''



@app.route('/addstaff1',methods=['post'])
def addstaff1():
    staffname=request.form['textfield']
    address=request.form['textfield2']
    place=request.form['textfield3']
    mobile = request.form['textfield4']

    gender=request.form['radiobutton']
    email=request.form['textfield6']
    usename = request.form['username']
    password = request.form['password']

    qry="insert into login values(null,%s,%s,'staff')"
    val=(usename,password)
    id=iud(qry,val)
    q="INSERT INTO `staff` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    va=(str(id),staffname,mobile,gender,email,place,address)

    iud(q,va)
    return ''' <script>alert("success");window.location="/managestaff"</script>'''




@app.route('/updatestaff1',methods=['post'])
def updatestaff1():
    staffname=request.form['textfield']
    address=request.form['textfield2']
    place=request.form['textfield3']
    mobile = request.form['textfield4']

    gender=request.form['radiobutton']
    email=request.form['textfield6']

    q="UPDATE `staff` SET `staff_name`=%s,`mobile`=%s,`gender`=%s,`email`=%s,`place`=%s,`address`=%s WHERE `staff_id`=%s"
    va=(staffname,mobile,gender,email,place,address,session['stid'])

    iud(q,va)
    return ''' <script>alert("success");window.location="/managestaff"</script>'''



@app.route('/addservice1',methods=['post'])
def addservice1():
    servicename=request.form['textfield']
    amount=request.form['textfield2']
    description=request.form['textfield3']

    q="INSERT INTO `services` VALUES(NULL,%s,%s,%s)"
    va=(servicename,amount,description)

    iud(q,va)
    return ''' <script>alert("success");window.location="/updateservice"</script>'''


@app.route('/addrequirements1',methods=['post'])
def addrequirements1():
    certificate=request.form['select']
    document=request.form['textfield2']

    q="INSERT INTO `requirements` VALUES(NULL,%s,%s)"
    va=(certificate,document)

    iud(q,va)
    return ''' <script>alert("success");window.location="/addrequirements"</script>'''

@app.route('/addtax1',methods=['post'])
def addtax1():
    user=request.form['textfield']
    taxtype=request.form['textfield22']
    amount=request.form['textfield23']
    date=request.form['textfield2']



    q="INSERT INTO `tax_info` VALUES(NULL,%s,%s,%s,%s)"
    va=(taxtype,amount,date,user)

    iud(q,va)
    return ''' <script>alert("success");window.location="/managetax"</script>'''


# @app.route('/upldcertficate1',methods=['post'])
# def upldcertficate1():
#     certificate = request.files['file']
#     finame = secure_filename(certificate.filename)
#     certificate.save(os.path.join('static/image', finame))
#
#     q="INSERT INTO `certificate` VALUES(NULL,%s,%s,curdate())"
#     va= (session['reqqid'],finame)
#
#     iud(q,va)
#     return ''' <script>alert("success");window.location="/verifypay"</script>'''


@app.route('/birth1',methods=['post'])
def birth1():
    signature = request.files['file']
    finame = secure_filename(signature.filename)
    signature.save(os.path.join('static/image', finame))

    dob=request.form['textfield']
    sex=request.form['radiobutton']
    name=request.form['textfield2']
    fname = request.form['textfield3']
    mname = request.form['textfield4']
    address1 = request.form['textfield5']
    address2 = request.form['textfield6']
    pob = request.form['textfield7']
    iname = request.form['textfield8']


    q="INSERT INTO `birth_certificate` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    va= (session['lid'],dob,sex,name,fname,mname,address1,address2,pob,iname,finame)

    iud(q,va)

    qry = "INSERT INTO `service_request` VALUES(NULL,CURDATE(),'pending',%s,%s)"
    val = (session['lid'], session['serid'])
    iud(qry, val)
    return ''' <script>alert("success");window.location="/upldocs#about"</script>'''


@app.route('/death1', methods=['post'])
def death1():
        signature = request.files['file']
        finame = secure_filename(signature.filename)
        signature.save(os.path.join('static/image', finame))
        dod = request.form['a']
        dname = request.form['b']
        address1 = request.form['c']
        fname = request.form['d']
        mname = request.form['e']
        # address2 = request.form['textfield5']
        sex = request.form['radiobutton']

        age = request.form['f']
        pod = request.form['select']
        loc = request.form['g']
        iname = request.form['h']
        iaddress = request.form['i']
        q ="INSERT INTO `death_certificate` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,CURDATE(),%s,%s)"
        va =(session['lid'],dod,dname,address1,fname,sex,age,pod,loc,iname,iaddress,finame,mname)
        iud(q,va)

        qry="INSERT INTO `service_request` VALUES(NULL,CURDATE(),'pending',%s,%s)"
        val=(session['lid'],session['serid'])
        iud(qry,val)
        return ''' <script>alert("success");window.location="/upldocsdeath#about"</script>'''



@app.route('/marriage1', methods=['post'])
def marriage1():
    localarea = request.form['lc']
    village = request.form['textfield']
    taluk = request.form['textfield4']
    dis = request.form['textfield5']
    date = request.form['textfield2']
    pm = request.form['textfield3']

    hname = request.form['textfield6']
    nationality1 = request.form['textfield63']
    occupation1 = request.form['textfield69']
    peradrs1 = request.form['textfield611']
    preads1 = request.form['textfield613']
    marital1 = request.form['select']
    spouse1 = request.form['radiobutton']
    signature1 = request.files['file']
    finame = secure_filename(signature1.filename)
    signature1.save(os.path.join('static/image', finame))
    fname1 = request.form['textfield6132']
    mname1 = request.form['textfield6133']
    witness1 = request.form['textfield61332']
    witness2 = request.form['textfield61333']
    address1 = request.form['textfield61334']
    addreess2 = request.form['textfield61335']
    signature3 = request.files['file3']
    finame2 = secure_filename(signature3.filename)
    signature3.save(os.path.join('static/image', finame2))
    signature4 = request.files['file32']
    finame3 = secure_filename(signature4.filename)
    signature4.save(os.path.join('static/image', finame3))
    wname = request.form['textfield62']
    nationalit2 = request.form['textfield64']
    occupation2 = request.form['textfield610']
    peradrs2 = request.form['textfield612']
    preads2 = request.form['textfield614']
    marital2 = request.form['select2']
    spouse2 = request.form['radiobutton1']
    signature2 = request.files['file2']
    finame4 = secure_filename(signature2.filename)
    signature2.save(os.path.join('static/image', finame4))
    fname2 = request.form['textfield6134']
    mname2 = request.form['textfield6135']

    photo1 = request.files['file00']
    finame5 = secure_filename(photo1.filename)
    photo1.save(os.path.join('static/image', finame5))

    photo2 = request.files['file01']
    finame6 = secure_filename(photo2.filename)
    photo2.save(os.path.join('static/image', finame6))


    age1 = request.form['textfield65']
    age2 = request.form['textfield66']
    dob1 = request.form['textfield67']
    dob2 = request.form['textfield68']

    q ="INSERT INTO `marriage_certificate` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    va =(session['lid'],date,hname,nationality1,occupation1,peradrs1,preads1,marital1,spouse1,finame,fname1,mname1,witness1,witness2,address1,addreess2,finame2,finame3,wname,nationalit2,occupation2,preads2,peradrs2,marital2,spouse2,finame4,fname2,mname2,finame5,finame6,localarea,village,taluk,dis,age1,age2,dob1,dob2)
    iud(q,va)

    qry = "INSERT INTO `service_request` VALUES(NULL,CURDATE(),'pending',%s,%s)"
    val = (session['lid'], session['serid'])
    iud(qry, val)

    return ''' <script>alert("success");window.location="/upldocs#about"</script>'''

@app.route('/ownership1',methods=['post'])
def ownership1():


    bid=request.form['textfield8']
    locabody=request.form['textfield7']
    zonaloffice=request.form['textfield6']
    wardno = request.form['textfield5']
    owner = request.form['textfield4']
    date = request.form['textfield3']
    fuctionality = request.form['textfield2']
    category = request.form['textfield']
    purpose = request.form['select']


    q="INSERT INTO `ownership_certificate` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    va= (session['lid'],bid,locabody,zonaloffice,wardno,owner,date,fuctionality,category,purpose)

    iud(q,va)
    return ''' <script>alert("success");window.location="/userhome"</script>'''


@app.route('/addcomplaint1',methods=['post'])
def addcomplaint1():
    complaint=request.form['textfield']
    q="INSERT INTO `complaints` VALUES(NULL,%s,'pending',CURDATE(),%s)"
    va=(complaint,session['lid'])

    iud(q,va)
    return ''' <script>alert("success");window.location="/userhome"</script>'''

@app.route('/deleteservice')
def deleteservice():
    id=request.args.get('id')
    qry="delete from services where service_id=%s"
    iud(qry,id)
    return ''' <script>alert("deleted");
               window.location="/updateservice"</script>'''

@app.route('/deletetax')
def deletetax():
    id=request.args.get('id')
    qry="delete from tax_info where tax_id=%s"
    iud(qry,id)
    return ''' <script>alert("deleted");
               window.location="/managetax"</script>'''

@app.route('/editservice')
def editservice():
    id = request.args.get('id')
    session['servid'] = id
    qry = "select * from services where service_id=%s"
    res = selectone(qry, id)
    return render_template("admin/editservice.html",val=res)



@app.route('/updateservice1',methods=['post'])
def updateservice1():
    servicename=request.form['textfield']
    amount=request.form['textfield2']
    description=request.form['textfield3']

    q="UPDATE `services` SET `service_name`=%s,`amount`=%s,`description`=%s WHERE `service_id`=%s"
    va=(servicename,amount,description,session['servid'])

    iud(q,va)
    return ''' <script>alert("success");window.location="/updateservice"</script>'''


@app.route('/editstaff')
def editstaff():
    id=request.args.get('id')
    session['stid']=id
    qry="select * from staff where staff_id=%s"
    res=selectone(qry,id)
    return render_template("admin/editstaff.html",val=res)








@app.route('/edittax')
def edittax():
    id = request.args.get('id')
    session['taxid'] = id
    qry = "select * from tax_info where tax_id=%s"
    res = selectone(qry, id)
    return render_template("admin/edittax.html",val=res)


@app.route('/updatetax',methods=['post'])
def updatetax():

    taxtype=request.form['textfield22']
    amount=request.form['textfield23']
    date=request.form['textfield2']



    q="UPDATE `tax_info` SET `type`=%s,`amount`=%s,`date`=%s WHERE `tax_id`=%s"
    va=(taxtype,amount,date,session['taxid'])

    iud(q,va)
    return ''' <script>alert("success");window.location="/managetax"</script>'''

@app.route('/reply')
def reply():
    id = request.args.get('id')
    session['CM_id'] = id

    return render_template("admin/reply.html")




@app.route('/updreply',methods=['post'])
def updreply():
    reply=request.form['textfield']

    q=" UPDATE `complaints` SET `reply`=%s WHERE `complaint_id`=%s"
    va=(reply,session['CM_id'])

    iud(q,va)
    return ''' <script>alert("success");window.location="/viewcomplaints"</script>'''

@app.route('/viewbirth')
def viewbirth():
     q = "select * from `birth_certificate` join `service_request` on `service_request`.`user_id`=`birth_certificate`.`user_id` where `service_request`.`request_id`=%s"
     res = selectone(q, session['EEE_id'])
     return render_template("staff/viewbirth.html",val=res)

@app.route('/viewdeath')
def viewdeath():
    q="SELECT * FROM `death_certificate` JOIN `service_request` ON `service_request`.`user_id`=`death_certificate`.`user_id` WHERE `service_request`.`request_id`=%s"
    res=selectone(q,session['EEE_id'])
    return render_template("staff/viewdeath.html",val=res)

@app.route('/viewmarriage')
def viewmarriage():
    q = "SELECT * FROM `marriage_certificate` JOIN `service_request` ON `service_request`.`user_id`=`marriage_certificate`.`user_id` WHERE `service_request`.`request_id`=%s"
    res = selectone(q, session['EEE_id'])
    return render_template("staff/viewmarriage.html",val=res)

@app.route('/viewownership')
def viewownership():
    q="SELECT * FROM `ownership_certificate` JOIN `service_request` ON `service_request`.`user_id`=`ownership_certificate`.`user_id` WHERE `service_request`.`request_id`=%s"
    res=selectone(q,session['EEE_id'])
    return render_template("staff/viewownership.html",val=res)

@app.route('/upldocsdeath')
def upldocsdeath():
    return render_template("user/upload death documents.html")




@app.route('/user_pay_proceed', methods=['post','get'])

def user_pay_proceed():
    import razorpay
    amount=session['pay_amount']

    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': amount+"00", 'currency': "INR", 'payment_capture': '1'})
    qry = "select * from user where lid=%s"
    res = selectone(qry, session['lid'])
    return render_template('user/UserPayProceed.html', p=payment,val=res)


@app.route('/on_payment_success', methods=['post'])

def on_payment_success():
    amt = session['pay_amount']
    qry = "INSERT INTO `tax_payment` VALUES(NULL,%s,%s,%s,CURDATE(),%s)"
    iud(qry, ( amt,session['taxid'],session['lid'],session['year']))

    # qry = "UPDATE `charity_information` SET `amount`=`amount`-%s WHERE `id`=%s"
    # iud(qry, (amt,charity))

    return '''<script>alert("Success! Thank you for your Contribution");window.location="userhome"</script>'''


@app.route('/chooseyear')
def chooseyear():
    amount = request.args.get('amt')
    id = request.args.get('id')
    session['taxid'] = id
    session['pay_amount'] = amount
    return render_template("user/chooseyear.html")

@app.route('/chooseyear1',methods=['post'])
def chooseyear1():
    year=request.form['textfield']
    session['year']=year

    res = selectone("SELECT * FROM `tax_payment` WHERE `tax_id`=%s AND `year`=%s AND `user_id`=%s",(session['taxid'],year,session['lid']))
    if res is None:
        return redirect('/user_pay_proceed')
    else:
        return '''<script>alert("Already Paid");window.location="viewtax#about"</script>'''


@app.route('/user_pay_proceed1', methods=['post','get'])

def user_pay_proceed1():
    import razorpay
    amount = session['samt']
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': amount+"00", 'currency': "INR", 'payment_capture': '1'})
    qry = "select * from user where lid=%s"
    res = selectone(qry, session['lid'])
    return render_template('user/UserPayProceed1.html', p=payment,val=res)



@app.route('/on_payment_success1', methods=['post'])
def on_payment_success1():
    amt = session['samt']
    qry = "INSERT INTO `payment` VALUES(NULL,%s,%s,CURDATE(),%s)"
    iud(qry, ( session['samt'],session['EEE_id'],session['lid']))

    # qry = "UPDATE `charity_information` SET `amount`=`amount`-%s WHERE `id`=%s"
    # iud(qry, (amt,charity))

    return '''<script>alert("Payement success");window.location="userhome"</script>'''



@app.route('/acceptapplicationrequest')
def acceptapplicationrequest():
    id=request.args.get('id')
    q="UPDATE `service_request` SET `status`='accepted' WHERE `request_id`=%s"
    iud(q,id)
    return '''<script>alert("Accepted");window.location="userhome"</script>'''

@app.route('/rejectapplicationrequest')
def rejectapplicationrequest():
    id=request.args.get('id')
    q="UPDATE `service_request` SET `status`='accepted' WHERE `request_id`=%s"
    iud(q,id)
    return '''<script>alert("Rejected");window.location="userhome"</script>'''




@app.route('/generate')
def generate():
    rid = request.args.get('id')
    res = selectone("select * from service_request where request_id=%s",rid)

    print(res['service_id'],"eeeeeeeeeeeeeeeeeeee")
    if str(res['service_id'])=="1":
        res1 = selectone("select *,curdate() as d from birth_certificate where user_id=%s",res['user_id'])
        return render_template("staff/generate_birth1.html",val=res1)
    elif str(res['service_id']) == "2":
        res = selectone("select *,curdate() as d from marriage_certificate where user_id=%s",res['user_id'])
        return render_template("staff/generate_marriage1.html",val=res)

    elif str(res['service_id']) == "3":
        res = selectone("select *,curdate() as d from ownership_certificate where user_id=%s",res['user_id'])
        return render_template("staff/generate_ownership1.html", val=res)

    else:
        res1 = selectone("select *,curdate() as d from death_certificate where user_id=%s",res['user_id'])
        return render_template("staff/generate_death1.html", val=res1)




app.run(debug=True)