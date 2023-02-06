<?php 
include "connect.php";

if (isset($_GET['del_id'])) {
	$id = $_GET['del_id'];

	$del_pasien = "delete from obat where id_obat = $id";
	$res = mysqli_query($con,$del_pasien);
	if ($res) {
      header('location:obat.php');
		
	}
	else{
		die(mysql_error($con));
	}

}

 ?>