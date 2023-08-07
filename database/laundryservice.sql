-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2023 at 06:33 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `laundryservice`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `name` text NOT NULL,
  `email` text NOT NULL,
  `password` varchar(20) NOT NULL,
  `address` text NOT NULL,
  `user_type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`name`, `email`, `password`, `address`, `user_type`) VALUES
('journeyfor infinity', 'salabibneawaliam@gmail.com', 'sssss', 'ssss', 'Delivery Man'),
('salab ibne awal eam', 'salabibneawaliam@gmail.com', '456987', 'banasree,dhaka', 'Customer'),
('abc', 'abc@gmail.com', '897', 'fg', 'Laundry service provider'),
('mithila ', 'mithgilka@gmail.com', '222', 'banasree,dhaka', 'Customer'),
('fgh', 'bb@gmail.com', '', 'mohakhali', 'Laundry service provider'),
('tasir', 'tasir@gmail.com', '789', 'vcfcdxe', 'Laundry service provider'),
('klm', 'klm@gmail.com', '222', 'mohakhali', 'Laundry service provider'),
('bnm', 'bnm@gmail.com', '123', 'banasree,dhaka', 'Delivery Man');

-- --------------------------------------------------------

--
-- Table structure for table `service`
--

CREATE TABLE `service` (
  `business_name` text NOT NULL,
  `service_1` text NOT NULL,
  `service_1_price` int(11) NOT NULL,
  `service_2` text NOT NULL,
  `service_2_price` int(11) NOT NULL,
  `service_3` text NOT NULL,
  `service_3_price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service`
--

INSERT INTO `service` (`business_name`, `service_1`, `service_1_price`, `service_2`, `service_2_price`, `service_3`, `service_3_price`) VALUES
('abc ', 'a', 5, 'b', 10, 'c', 150),
('abc ', 'a', 5, 'b', 10, 'c', 150),
('abc ', 'a', 5, 'b', 10, 'c', 150);

-- --------------------------------------------------------

--
-- Table structure for table `service_provider`
--

CREATE TABLE `service_provider` (
  `business_name` text NOT NULL,
  `service-1` text NOT NULL,
  `service_1_price` int(30) NOT NULL,
  `service_2` text NOT NULL,
  `service_2_price` int(11) NOT NULL,
  `service_3` text NOT NULL,
  `service_3_price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD UNIQUE KEY `adress` (`name`(50));

--
-- Indexes for table `service_provider`
--
ALTER TABLE `service_provider`
  ADD PRIMARY KEY (`business_name`(50));
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
