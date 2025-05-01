CREATE DATABASE IF NOT EXISTS document_qa;
USE document_qa;

CREATE TABLE documents (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content TEXT
);

INSERT INTO documents (content) VALUES
('This is a sample document about Kubernetes.'),
('This document explains what Redis is used for.'),
('Python is a great programming language for building APIs.');

SHOW TABLES;

SELECT * FROM documents;