<?php
$servername = "192.168.99.100:3306";
$username = "app_db_user";
$password = "123";
$dbname = "app_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
?>