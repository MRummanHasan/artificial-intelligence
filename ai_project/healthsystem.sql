-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2018 at 05:16 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 5.6.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthsystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `diseases`
--

CREATE TABLE `diseases` (
  `disease_ID` int(5) NOT NULL,
  `disease_Name` varchar(20) NOT NULL,
  `disease_mainSymp` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diseases`
--

INSERT INTO `diseases` (`disease_ID`, `disease_Name`, `disease_mainSymp`) VALUES
(1, 'Disease1', 'Deep Cough'),
(2, 'Disease2', 'Jaw Pain'),
(3, 'Disease3', 'MainSymp3'),
(4, 'Disease4', 'Nose Bleeding'),
(5, 'Disease5', 'Swelling in Cheeck'),
(6, 'Disease6', 'Red or Mouth Patch i');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `doc_ID` int(5) NOT NULL,
  `doc_name` varchar(20) NOT NULL,
  `doc_dept` varchar(20) NOT NULL,
  `doc_TimeTo` varchar(20) NOT NULL,
  `doc_timeFrom` varchar(20) NOT NULL,
  `doc_location` varchar(30) NOT NULL,
  `doc_price` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doc_ID`, `doc_name`, `doc_dept`, `doc_TimeTo`, `doc_timeFrom`, `doc_location`, `doc_price`) VALUES
(1, 'Fahad', 'ENT', '1200', '1400', 'Nazimabad Hospital', '500'),
(2, 'Hammad', 'ENT', '0700', '1000', 'Johar Hospital', '300'),
(3, 'Masood', 'Surgeon', '0600', '0800', 'DHA Hospital', '1000'),
(4, 'Amin', 'Skin', '0300', '0500', 'Saddar Skin Hospital', '150'),
(5, 'Rayyan', 'Cancer', '0900', '1400', 'Nazimabad Hospital', '750'),
(6, 'Samayan', 'Dentist', '0900', '1500', 'Nazimabad Hospital', '800'),
(7, 'Rayyan', 'General', '0900', '1700', 'Johar Hospital', '150'),
(8, 'John', 'General', '1700', '2400', 'Nazimabad Hospital', '200');

-- --------------------------------------------------------

--
-- Table structure for table `junct_disease_symptom`
--

CREATE TABLE `junct_disease_symptom` (
  `disease_id` int(5) NOT NULL,
  `symptom_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `junct_disease_symptom`
--

INSERT INTO `junct_disease_symptom` (`disease_id`, `symptom_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 6),
(2, 7),
(3, 8),
(3, 9),
(3, 10),
(3, 11),
(3, 12),
(1, 4),
(2, 4),
(3, 8),
(2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `precaution`
--

CREATE TABLE `precaution` (
  `med_id` int(11) NOT NULL,
  `firstname` varchar(20) NOT NULL,
  `scientificname` varchar(55) NOT NULL,
  `power` varchar(7) NOT NULL,
  `company` varchar(10) NOT NULL,
  `date_of_expiry` varchar(15) NOT NULL,
  `picture` varchar(999) NOT NULL,
  `date_of_manufacture` varchar(15) NOT NULL,
  `sex` varchar(8) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `symptoms`
--

CREATE TABLE `symptoms` (
  `symptom_id` int(11) NOT NULL,
  `symptoms_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `symptoms`
--

INSERT INTO `symptoms` (`symptom_id`, `symptoms_name`) VALUES
(1, 'Ear Pain'),
(2, 'Sore Swelling'),
(3, 'Change in Voice'),
(4, 'Difficulty in Breath'),
(5, 'Sore Throat'),
(6, 'Teeth Loose'),
(7, 'Painful Chewing'),
(8, 'Weakness'),
(9, 'Fever'),
(10, 'Cheek Swelling');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `diseases`
--
ALTER TABLE `diseases`
  ADD PRIMARY KEY (`disease_ID`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`doc_ID`);

--
-- Indexes for table `junct_disease_symptom`
--
ALTER TABLE `junct_disease_symptom`
  ADD KEY `symptom_id` (`symptom_id`),
  ADD KEY `disease_id` (`disease_id`);

--
-- Indexes for table `precaution`
--
ALTER TABLE `precaution`
  ADD PRIMARY KEY (`med_id`);

--
-- Indexes for table `symptoms`
--
ALTER TABLE `symptoms`
  ADD PRIMARY KEY (`symptom_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diseases`
--
ALTER TABLE `diseases`
  MODIFY `disease_ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `precaution`
--
ALTER TABLE `precaution`
  MODIFY `med_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `junct_disease_symptom`
--
ALTER TABLE `junct_disease_symptom`
  ADD CONSTRAINT `junct_disease_symptom_ibfk_1` FOREIGN KEY (`disease_id`) REFERENCES `diseases` (`disease_ID`),
  ADD CONSTRAINT `junct_disease_symptom_ibfk_2` FOREIGN KEY (`disease_id`) REFERENCES `symptoms` (`symptom_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
