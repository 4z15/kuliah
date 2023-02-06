<?php
include "connect.php";
$id = $_GET['upd_id'];
// SELECT p.nama_pasien, p.alamat,r.keluhan,r.diagnosa,r.obat,r.tanggal
// FROM pasien p
// INNER JOIN rekam_medis r ON r.id_pasien = p.id_pasien;

// UPDATE `rekam_medis` SET `keluhan`='pusing',`diagnosa`='vertigo',`obat`='fatigon',`tanggal`='01/17/2023' WHERE id_rekam_medis=4;
$sel_pasien = "SELECT 
p.nama_pasien, 
p.alamat,
r.keluhan,
r.diagnosa,
r.obat,
r.tanggal
FROM pasien p
INNER JOIN rekam_medis r
ON r.id_pasien = p.id_pasien where r.id_rekam_medis = $id";

$res = mysqli_query($con,$sel_pasien);
$row = mysqli_fetch_assoc($res);

$alamat = $row['alamat'];
$nama = $row['nama_pasien'];
$keluhan = $row['keluhan'];
$diagnosa = $row['diagnosa'];
$obat = $row['obat'];
$tanggal = $row['tanggal'];



if (isset($_POST['submit'])){
	$nama = $_POST['name'];
	$diagnosa = $_POST['diagnosa'];
	$keluhan = $_POST['keluhan'];
	$tanggal = $_POST['tanggal'];
	$obat = $_POST['obat'];
	$alamat = $_POST['alamat'];

	// query update pasien&rekam_medis
	$upd_rek_medis = "UPDATE pasien,rekam_medis SET 
	pasien.nama_pasien='$nama',
	pasien.alamat = '$alamat' , 
	rekam_medis.diagnosa='$diagnosa',
	rekam_medis.obat='$obat',
	rekam_medis.tanggal='$tanggal',
	rekam_medis.keluhan='$keluhan'
	WHERE pasien.id_pasien = rekam_medis.id_pasien AND rekam_medis.id_rekam_medis=$id ";
	$res2 = mysqli_query($con,$upd_rek_medis);
	if($res2){
      header('location:rekam_medis.php');
		// echo "updated";

	}else{
		die(mysqli_error($con));
	}



}


?>


<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Patient</title>

    <!-- Custom fonts for this template-->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="css/sb-admin-2.min.css" rel="stylesheet">

</head>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
        <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

            <!-- Sidebar - Brand -->
            <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.php">
                <div class="sidebar-brand-icon rotate-n-15">
                    <i class="fas fa-laugh-wink"></i>
                </div>
                <div class="sidebar-brand-text mx-3">E Puskesmas <sup></sup></div>
            </a>

            <!-- Divider -->
            <hr class="sidebar-divider my-0">

            <!-- Nav Item - Dashboard -->
            <li class="nav-item active">
                <a class="nav-link" href="index.php">
                    <i class="fas fa-fw fa-tachometer-alt"></i>
                    <span>Dashboard</span></a>
            </li>

            <!-- Divider -->
            <hr class="sidebar-divider">

            <!-- Heading -->
            <div class="sidebar-heading">
                Interface
            </div>

            <!-- Nav Item - Pages Collapse Menu -->
            <li class="nav-item">
                <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseTwo"
                    aria-expanded="true" aria-controls="collapseTwo">
                    <i class="fas fa-fw fa-cog"></i>
                    <span>Admin</span>
                </a>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">
                    <div class="bg-white py-2 collapse-inner rounded">
                        <!-- <h6 class="collapse-header">Custom Components:</h6> -->
                        <a class="collapse-item" href="add_pasien.php">Registration</a>
                        <a class="collapse-item" href="pasien.php">Patient</a>
                    </div>
                </div>
            </li>
            <li class="nav-item">
                <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseTwo"
                    aria-expanded="true" aria-controls="collapseTwo">
                    <i class="fas fa-fw fa-cog"></i>
                    <span>Nurse</span>
                </a>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">
                    <div class="bg-white py-2 collapse-inner rounded">
                        <!-- <h6 class="collapse-header">Custom Components:</h6> -->
                        <a class="collapse-item" href="obat.php">Medicine</a>
                        <a class="collapse-item" href="pemberian_obat.php">Medicine Administration</a>

                        <a class="collapse-item" href="transaksi.php">Transaction</a>
                    </div>
                </div>
            </li>
            <li class="nav-item">
                <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseTwo"
                    aria-expanded="true" aria-controls="collapseTwo">
                    <i class="fas fa-fw fa-cog"></i>
                    <span>Docter</span>
                </a>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">
                    <div class="bg-white py-2 collapse-inner rounded">
                        <!-- <h6 class="collapse-header">Custom Components:</h6> -->
                        <a class="collapse-item" href="rekam_medis.php">Medical Records</a>
                        <a class="collapse-item" href="add_rekam_medis.php">Add Medical Records</a>

                        <!-- <a class="collapse-item" href="cards.html">Docter</a> -->
                    </div>
                </div>
            </li>
            <li class="nav-item">
                <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseTwo"
                    aria-expanded="true" aria-controls="collapseTwo">
                    <i class="fas fa-fw fa-cog"></i>
                    <span>Report</span>
                </a>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">
                    <div class="bg-white py-2 collapse-inner rounded">
                        <!-- <h6 class="collapse-header">Custom Components:</h6> -->
                        <a class="collapse-item" href="laporan.php">Report</a>
                        <!-- <a class="collapse-item" href="cards.html">Docter</a> -->
                    </div>
                </div>
            </li>

           

          

            <!-- Divider -->
            <hr class="sidebar-divider d-none d-md-block">

            <!-- Sidebar Toggler (Sidebar) -->
            <div class="text-center d-none d-md-inline">
                <button class="rounded-circle border-0" id="sidebarToggle"></button>
            </div>

        </ul>
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->
                <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">

                    <!-- Sidebar Toggle (Topbar) -->
                    <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3">
                        <i class="fa fa-bars"></i>
                    </button>

                    <!-- Topbar Search -->
                <!--     <form
                        class="d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search">
                        <div class="input-group">
                            <input type="text" class="form-control bg-light border-0 small" placeholder="Search for..."
                                aria-label="Search" aria-describedby="basic-addon2">
                            <div class="input-group-append">
                                <button class="btn btn-primary" type="button">
                                    <i class="fas fa-search fa-sm"></i>
                                </button>
                            </div>
                        </div>
                    </form> -->

                    <!-- Topbar Navbar -->
                    <ul class="navbar-nav ml-auto">

                       
                        <div class="topbar-divider d-none d-sm-block"></div>

                        <!-- Nav Item - User Information -->
                        <li class="nav-item dropdown no-arrow">
                            <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <span class="mr-2 d-none d-lg-inline text-gray-600 small">Admin</span>
                                <img class="img-profile rounded-circle"
                                    src="img/undraw_profile.svg">
                            </a>
                            <!-- Dropdown - User Information -->
                            <div class="dropdown-menu dropdown-menu-right shadow animated--grow-in"
                                aria-labelledby="userDropdown">
                           
                                <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">
                                    <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                    Logout
                                </a>
                            </div>
                        </li>

                    </ul>

                </nav>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <!-- Page Heading -->
                    <div class="d-sm-flex align-items-center justify-content-between mb-3">
                        <h1 class="h3 mb-0 text-gray-800">Patient</h1>
                    <!--     <a href="index.php" class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm"><i
                                class="fas fa-download fa-sm text-white-50"></i> Generate Report</a> -->
                    </div>


                    <!-- Content Row -->
                    <div class="row">
<div class="container">
			<form method="POST" >

				<div class="mb-3 my-3">
					<label >Name</label>
					<input type="text" class="form-control" name ="name" value=<?php 
					echo $nama;
					 ?>>
				</div>
				<div class="mb-3">
					<label >Address</label>
					<input type="text" class="form-control"  name ="alamat" value=<?php 
					echo $alamat;
					 ?>>
				</div>
				<div class="mb-3"> 
					<label >Complaints</label>
					<input type="text" class="form-control"  name="keluhan" value=<?php 
					echo $keluhan;
					 ?>>
				</div>
				<div class="mb-3">
					<label >Diagnose</label>
                    <input type="text" class="form-control" name="diagnosa" 
                    value=<?php 
					echo $diagnosa;
					 ?>
                    >
				</div>
				<div class="mb-3">
					<label >Medicine</label>
					<!-- <input type="text" class="form-control" placeholder="Enter your address" name="address"> -->
                    <input type="text" name="obat" class="form-control" 
					value=<?php 
					echo $obat;
					 ?>>
				</div>
                <div class="mb-3">
					<label >Date</label>
					<!-- <input type="text" class="form-control" placeholder="Enter your address" name="address"> -->
                    <input type="date" name="tanggal" class="form-control" 
					value=<?php 
					echo $tanggal;
					 ?>>
				</div>

				<button type="submit" class="btn btn-primary" name="submit">Update</button>
			</form>
		</div>


                    </div> 

                    <!-- Content Row -->


                         </div>
                        <!-- </div>  -->

                            </div>
                        <!-- </div> --> 
             

                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <!-- Footer -->
            <footer class="sticky-footer bg-white">
                <div class="container my-auto">
                    <div class="copyright text-center my-auto">
                        <span>Copyright &copy; E_Puskesmas</span>
                    </div>
                </div>
            </footer>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">×</span>
                    </button>
                </div>
                <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
                <div class="modal-footer">
                    <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                    <a class="btn btn-primary" href="login.php">Logout</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin-2.min.js"></script>

    <!-- Page level plugins -->
    <script src="vendor/chart.js/Chart.min.js"></script>

    <!-- Page level custom scripts -->
    <script src="js/demo/chart-area-demo.js"></script>
    <script src="js/demo/chart-pie-demo.js"></script>

</body>

</html>