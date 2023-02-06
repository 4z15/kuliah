<?php 
include "connect.php";

if (isset($_GET['del_id'])) {
	$id = $_GET['del_id'];

	$del_rek_medis = "delete from rekam_medis where id_rekam_medis = $id";
	$res = mysqli_query($con,$del_rek_medis);
	if ($res) {
      header('location:rekam_medis.php');
		
	}
	else{
		die(mysql_error($con));
	}

}

 ?>