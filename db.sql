/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - egram
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`egram` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `egram`;

/*Table structure for table `birth_certificate` */

DROP TABLE IF EXISTS `birth_certificate`;

CREATE TABLE `birth_certificate` (
  `birth_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `sex` varchar(20) DEFAULT NULL,
  `child_name` varchar(20) DEFAULT NULL,
  `father_name` varchar(20) DEFAULT NULL,
  `mother_name` varchar(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `address2` varchar(100) DEFAULT NULL,
  `birth_place` varchar(50) DEFAULT NULL,
  `informant_name` varchar(20) DEFAULT NULL,
  `informant_signaturae` text,
  PRIMARY KEY (`birth_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `birth_certificate` */

insert  into `birth_certificate`(`birth_id`,`user_id`,`dob`,`sex`,`child_name`,`father_name`,`mother_name`,`address`,`address2`,`birth_place`,`informant_name`,`informant_signaturae`) values 
(1,'2','2023-05-05','female','raza','anwar','lubna','yfguyf','yfiurmn','ems perinthalmanna','geee','FINAL_merged.pdf'),
(2,'11','2023-05-09','male','qwerty','hjujgh','fghghj','sgyjkl','ertfgyhujiko','fghjk','ertyguh','Degree_Prelims_Hall_Ticket.pdf');

/*Table structure for table `certificate` */

DROP TABLE IF EXISTS `certificate`;

CREATE TABLE `certificate` (
  `certificate_id` int(20) NOT NULL AUTO_INCREMENT,
  `rid` int(50) DEFAULT NULL,
  `certificate` varchar(1000) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`certificate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `certificate` */

insert  into `certificate`(`certificate_id`,`rid`,`certificate`,`date`) values 
(1,1,'QmcWC3mPsoRBZGWBVNhrrfnJF6f5qZbcqocXSj1q4iXgep','2023-05-10');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `user_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`complaint`,`reply`,`date`,`user_id`) values 
(1,'compl','kjhgv','2023-03-26',2),
(2,'2','pending','2023-03-27',0),
(3,'11','pending','2023-05-01',0),
(4,'11','pending','2023-05-01',0),
(5,'hii','ok','2023-05-01',11),
(6,'not working','pending','2023-05-10',11),
(7,'wertyuio','ok','2023-05-10',2);

/*Table structure for table `death_certificate` */

DROP TABLE IF EXISTS `death_certificate`;

CREATE TABLE `death_certificate` (
  `death_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(20) DEFAULT NULL,
  `death_date` date DEFAULT NULL,
  `name_of_deceased` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `name_of_f/h` varchar(50) DEFAULT NULL,
  `sex` varchar(50) DEFAULT NULL,
  `age` int(20) DEFAULT NULL,
  `place_of_death1` varchar(50) DEFAULT NULL,
  `place_of_death2` varchar(50) DEFAULT NULL,
  `informant_name` varchar(50) DEFAULT NULL,
  `informant_address` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `informant_signature` varchar(100) DEFAULT NULL,
  `name of mother` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`death_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `death_certificate` */

insert  into `death_certificate`(`death_id`,`user_id`,`death_date`,`name_of_deceased`,`address`,`name_of_f/h`,`sex`,`age`,`place_of_death1`,`place_of_death2`,`informant_name`,`informant_address`,`date`,`informant_signature`,`name of mother`) values 
(1,11,'2023-04-28','lkjihugf','hg','iouyh','female',30,'other','kkk','kjhgfg','huh','2023-05-01','Default.jpg','mh');

/*Table structure for table `documents` */

DROP TABLE IF EXISTS `documents`;

CREATE TABLE `documents` (
  `document_id` int(20) NOT NULL AUTO_INCREMENT,
  `document` varchar(100) DEFAULT NULL,
  `uid` int(100) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`document_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `documents` */

insert  into `documents`(`document_id`,`document`,`uid`,`type`,`status`) values 
(1,'uppa_LIC_2023_azeez_PaymentReceipt_1233790_.pdf',2,'parent\'s id proof','pending'),
(2,'uppa_LIC_2023_azeez_PaymentReceipt_1233790_.pdf',2,'parent\'s id proof','pending'),
(3,'jamal_LIC_2013_PaymentReceipt_1233012_.pdf',2,'parents marriage certificate','pending'),
(4,'Recommendation_Letter.pdf',11,'parents id proof','pending'),
(5,'Recommendation_Letter.pdf',11,'parents marriage certificate','pending'),
(6,'Recommendation_Letter.pdf',11,'parents marriage certificate','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(329) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'riya','riya','user'),
(3,'jalva','jalva','staff'),
(4,'jalva','jalva','staff'),
(5,'jalva','jalva','staff'),
(6,'jalva','jalva','staff'),
(7,'jalva','jalva','staff'),
(11,'asna','asna','user'),
(12,'staff','staff','staff');

/*Table structure for table `marriage_certificate` */

DROP TABLE IF EXISTS `marriage_certificate`;

CREATE TABLE `marriage_certificate` (
  `marriage_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(20) DEFAULT NULL,
  `marriage_date` varchar(20) DEFAULT NULL,
  `husband_name` varchar(20) DEFAULT NULL,
  `nationality1` varchar(20) DEFAULT NULL,
  `occupation1` varchar(50) DEFAULT NULL,
  `permenant_address1` varchar(100) DEFAULT NULL,
  `present_address1` varchar(100) DEFAULT NULL,
  `marital_status1` varchar(50) DEFAULT NULL,
  `spouse_no1` varchar(50) DEFAULT NULL,
  `signature1` varchar(100) DEFAULT NULL,
  `father_name1` varchar(50) DEFAULT NULL,
  `mother_name1` varchar(50) DEFAULT NULL,
  `witness1` varchar(50) DEFAULT NULL,
  `witness2` varchar(50) DEFAULT NULL,
  `address1` varchar(50) DEFAULT NULL,
  `address2` varchar(50) DEFAULT NULL,
  `witness_signature1` varchar(50) DEFAULT NULL,
  `witness_signature2` varchar(50) DEFAULT NULL,
  `wife_name` varchar(100) DEFAULT NULL,
  `nationality2` varchar(100) DEFAULT NULL,
  `occupation2` varchar(100) DEFAULT NULL,
  `permenant_address2` varchar(100) DEFAULT NULL,
  `present_address2` varchar(100) DEFAULT NULL,
  `marital_status2` varchar(100) DEFAULT NULL,
  `spouse_no2` varchar(100) DEFAULT NULL,
  `signature2` varchar(100) DEFAULT NULL,
  `father_name2` varchar(100) DEFAULT NULL,
  `mother_name2` varchar(100) DEFAULT NULL,
  `photo1` varchar(100) DEFAULT NULL,
  `photo2` varchar(100) DEFAULT NULL,
  `localarea` varchar(100) DEFAULT NULL,
  `village` varchar(100) DEFAULT NULL,
  `taluk` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `age1` varchar(100) DEFAULT NULL,
  `age2` varchar(100) DEFAULT NULL,
  `dob1` varchar(20) DEFAULT NULL,
  `dob2` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`marriage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `marriage_certificate` */

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(20) NOT NULL AUTO_INCREMENT,
  `content` varchar(1000) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`content`,`date`) values 
(1,'cbsdvb','2023-04-28'),
(2,'kjhg','2023-05-01'),
(3,'Latest News and Updates from Your Local Panchayat','2023-05-10'),
(4,'aaaaa','2023-05-10');

/*Table structure for table `ownership_certificate` */

DROP TABLE IF EXISTS `ownership_certificate`;

CREATE TABLE `ownership_certificate` (
  `ownership_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(50) DEFAULT NULL,
  `building_id` varchar(50) DEFAULT NULL,
  `localbody` varchar(50) DEFAULT NULL,
  `zonal_office` varchar(50) DEFAULT NULL,
  `ward_doorno` varchar(50) DEFAULT NULL,
  `owner` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `functionality` varchar(50) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `purpose` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ownership_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `ownership_certificate` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(20) NOT NULL AUTO_INCREMENT,
  `amount` int(100) DEFAULT NULL,
  `request_id` int(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `user_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`amount`,`request_id`,`date`,`user_id`) values 
(1,20,1,'2023-05-01',2),
(2,20,1,'2023-05-09',2),
(3,20,1,'2023-05-09',2),
(4,20,1,'2023-05-10',11);

/*Table structure for table `requirements` */

DROP TABLE IF EXISTS `requirements`;

CREATE TABLE `requirements` (
  `requirements_id` int(20) NOT NULL AUTO_INCREMENT,
  `service_id` int(20) DEFAULT NULL,
  `documents` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`requirements_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

/*Data for the table `requirements` */

insert  into `requirements`(`requirements_id`,`service_id`,`documents`) values 
(1,4,'birth certificate/SSLC'),
(2,4,'Adhaar card'),
(3,4,'Residential proof'),
(4,4,'ration card'),
(5,4,'Medical certification of cause of death'),
(6,4,'Applicant ID card'),
(7,2,'birth certificate/SSLC'),
(8,2,'Applicant ID card'),
(9,1,'parents id proof'),
(10,1,'parents marriage certificate'),
(11,3,'land tax receipt'),
(12,4,'aaaa');

/*Table structure for table `service_request` */

DROP TABLE IF EXISTS `service_request`;

CREATE TABLE `service_request` (
  `request_id` int(20) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `user_id` int(20) DEFAULT NULL,
  `service_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `service_request` */

insert  into `service_request`(`request_id`,`date`,`status`,`user_id`,`service_id`) values 
(1,'2023-05-09','uploaded',2,1),
(2,'2023-05-10','pending',11,1);

/*Table structure for table `services` */

DROP TABLE IF EXISTS `services`;

CREATE TABLE `services` (
  `service_id` int(20) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(100) DEFAULT NULL,
  `amount` int(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `services` */

insert  into `services`(`service_id`,`service_name`,`amount`,`description`) values 
(1,'birth',20,'fffff'),
(2,'marriage',10,'aaaaa'),
(3,'ownership',20,'aaaa'),
(4,'death',3000,'fddv');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(20) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `staff_name` varchar(50) DEFAULT NULL,
  `mobile` int(10) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`lid`,`staff_name`,`mobile`,`gender`,`email`,`place`,`address`) values 
(4,12,'staff',2147483647,'male','jaseelapp2492@gmail.com','tirur','Jaseela pp');

/*Table structure for table `tax_info` */

DROP TABLE IF EXISTS `tax_info`;

CREATE TABLE `tax_info` (
  `tax_id` int(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  `amount` int(100) DEFAULT NULL,
  `date` varchar(345) DEFAULT NULL,
  `user_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`tax_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tax_info` */

insert  into `tax_info`(`tax_id`,`type`,`amount`,`date`,`user_id`) values 
(1,'jalva',0,'0000-00-00',1234),
(2,'abu',0,'0000-00-00',12345),
(3,'c',34,'0000-00-00',0),
(6,'property tax',2500,'2023-05-10',2);

/*Table structure for table `tax_payment` */

DROP TABLE IF EXISTS `tax_payment`;

CREATE TABLE `tax_payment` (
  `taxpayment_id` int(50) NOT NULL AUTO_INCREMENT,
  `amount` int(50) DEFAULT NULL,
  `tax_id` int(50) DEFAULT NULL,
  `user_id` int(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `year` int(50) DEFAULT NULL,
  PRIMARY KEY (`taxpayment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tax_payment` */

insert  into `tax_payment`(`taxpayment_id`,`amount`,`tax_id`,`user_id`,`date`,`year`) values 
(1,12345,4,11,'2023-05-01',2021),
(2,2500,6,2,'2023-05-10',2023);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(20) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `dob` varchar(10) NOT NULL,
  `age` bigint(10) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `signature` varchar(100) NOT NULL,
  `house_no` varchar(20) NOT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `locality` varchar(20) NOT NULL,
  `post_office` varchar(50) NOT NULL,
  `pincode` bigint(20) NOT NULL,
  `district` varchar(20) NOT NULL,
  `taluk` varchar(20) NOT NULL,
  `village` varchar(20) NOT NULL,
  `father_name` varchar(20) DEFAULT NULL,
  `mother_name` varchar(20) DEFAULT NULL,
  `marital_status` varchar(20) DEFAULT NULL,
  `phone` bigint(10) NOT NULL,
  `email` varchar(20) NOT NULL,
  `driving_licenceno.` varchar(50) DEFAULT NULL,
  `passport_no` varchar(50) DEFAULT NULL,
  `sslc_regn0` varchar(50) DEFAULT NULL,
  `rationcard_no` varchar(50) DEFAULT NULL,
  `election_id` varchar(50) DEFAULT NULL,
  `adhar_no` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`lid`,`name`,`gender`,`dob`,`age`,`photo`,`signature`,`house_no`,`house_name`,`locality`,`post_office`,`pincode`,`district`,`taluk`,`village`,`father_name`,`mother_name`,`marital_status`,`phone`,`email`,`driving_licenceno.`,`passport_no`,`sslc_regn0`,`rationcard_no`,`election_id`,`adhar_no`) values 
(1,2,'riya','radiobutton','12/08/2000',22,'WhatsApp_Image_2022-05-01_at_8.34.01_PM.jpeg','WhatsApp_Image_2022-05-01_at_8.34.01_PM.jpeg','riya','iya','ya','a',5678,'jalva','alva','lva','va','a','no',919061892004,'jaseelapp2492@gmail.','aaa','aa','aaaa','aaaaaaaa','aaaa','aaaa'),
(2,11,'asna','female','',0,'WhatsApp_Image_2022-05-01_at_8.34.01_PM.jpeg','WhatsApp_Image_2022-05-01_at_8.34.01_PM.jpeg','','','','',0,'','','','','','',9539987465,'','','','','','','');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
