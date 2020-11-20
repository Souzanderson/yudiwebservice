CREATE DATABASE `sensores`;
CREATE TABLE `steam_sensor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dssensor` varchar(450) NOT NULL,
  `steam_t_h` double(18,9) NOT NULL,
  `dtupdate` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM;

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hascode` longtext NOT NULL,
  `name` longtext NOT NULL,
  `email` longtext NOT NULL,
  `dtupdate` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM;
