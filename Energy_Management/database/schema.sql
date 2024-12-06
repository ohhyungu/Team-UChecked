-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS ems;

USE ems;

-- 센서 데이터 저장 테이블
CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_type VARCHAR(50) NOT NULL,
    value VARCHAR(100) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 명령 저장 테이블
CREATE TABLE commands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    command VARCHAR(100) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

