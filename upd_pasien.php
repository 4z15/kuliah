<?php
include "connect.php";
$id = $_GET['upd_id'];

$sel_pasien = "select * from pasien where id_pasien = $id";
$res = mysqli_query($con,$sel_pasien);
$row = mysqli_fetch_assoc($res);
$NIK = $row['nik'];
$nama = $row['nama_pasien'];
$no_telp = $row['no_telp'];
$jk = $row['j_kelamin'];
$addr = $row['alamat'];

if (isset($_POST['submit'])){
	$nama = $_POST['name'];
	$nik = $_POST['NIK'];
	$no_telp = $_POST['mobile'];
	$j_kelamin = implode("",$_POST['gender']);
	$alamat = $_POST['address'];

	$upd_pasien = "update pasien set nik = '$nik',nama_pasien ='$nama' ,no_telp = '$no_telp',alamat = '$alamat', j_kelamin = '$j_kelamin' where id_pasien = $id" ;
	$res = mysqli_query($con,$upd_pasien);
	if($res){
      header('location:pasien.php');
		// echo "updated";

	}else{
		die(mysqli_error($con));
	}



}


?>
<!doctype html>
	<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Pasien</title> 

		<!-- link boostrap -->
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

	</head>

	<body>
		<div class="container">
			<form method="POST" >

				<div class="mb-3 my-3">
					<label >Name</label>
					<input type="text" class="form-control" placeholder="Enter your name" name = "name" value=<?php 
					echo $nama;
					 ?>>
				</div>
				<div class="mb-3">
					<label >NIK</label>
					<input type="text" class="form-control" placeholder="Enter your NIK" name = "NIK" value=<?php 
					echo $NIK;
					 ?>>
				</div>
				<div class="mb-3"> 
					<label >Mobile</label>
					<input type="text" class="form-control" placeholder="Enter your mobile" name="mobile" value=<?php 
					echo $no_telp;
					 ?>>
				</div>
				<div class="mb-3">
					<label >Gender</label>
					<div class="form-check">
						<input class="form-check-input" type="checkbox"  name="gender[]" value="L" >
						<label class="form-check-label" >
							Male
						</label>
					</div>
					<div class="form-check">
						<input class="form-check-input" type="checkbox" name="gender[]" value="P" >
						<label class="form-check-label" >
							Female
						</label>
					</div>

				</div>
				<div class="mb-3">
					<label >Address</label>
					<!-- <input type="text" class="form-control" placeholder="Enter your address" name="address"> -->
					<textarea class="form-control"  rows="3" name="address"
					value=<?php 
					echo $addr;
					 ?>>
					 	
					 </textarea>

				</div>

				<button type="submit" class="btn btn-primary" name="submit">Update</button>
			</form>
		</div>

	</body>
	</html>

