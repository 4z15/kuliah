<?php 

$localhost ='localhost';
$username ='root';
$password ='';
$database ='E_Puskesmas';

$con = mysqli_connect($localhost,$username,$password,$database);

if (!$con) {
	die(mysqli_error($con));
	// code...
}
?>