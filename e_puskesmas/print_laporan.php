<!-- import modul connect.php  -->
<?php
include "connect.php";
// $keyword = $_GET['keyword'];
$sel_pasien = "SELECT rm.id_rekam_medis, p.nama_pasien,p.alamat,rm.keluhan, rm.diagnosa, rm.obat, rm.tanggal FROM `rekam_medis` rm INNER JOIN pasien p on rm.id_pasien = p.id_pasien "; 
            // $sel_pasien = "select id_pasien,nik,nama_pasien,no_telp,j_kelamin from pasien";
$result = mysqli_query($con,$sel_pasien);
if($result){
	while($row = mysqli_fetch_assoc($result)){ 
		$id = $row['id_rekam_medis'];
		$nama = $row['nama_pasien'];
		$alamat = $row['alamat'];
		$keluhan = $row['keluhan'];
		$diagnosa = $row['diagnosa'];
		$obat = $row['obat'];
		$tanggal = $row['tanggal'];
// $tgl = $result['tanggal'];


		?>
		<!doctype html>
			<html lang="en">
			<head>
				<meta charset="utf-8">
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<title>Report</title> 

				<!-- link boostrap -->
				<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

			</head>

			<body>
				<div class="container">
					<figure class="text-center">
						<blockquote class="blockquote">
							<p>MEDICAL RECORDS REPORT</p>
						</blockquote>
						<figcaption class="blockquote-footer">
							MEDICAL RECORDS REPORT IN <?php echo $tanggal; ?> 
						</figcaption>
					</figure>


					<table class="table">
						<thead>
							<tr>
								<th scope="col">Id</th>
								<th scope="col">Name</th>
								<th scope="col">Address</th>
								<th scope="col">Complaints</th>
								<th scope="col">Diagnose</th>
								<th scope="col">Medicine</th>
								<th scope="col">Date</th>
								<!-- <th scope="col">Operations</th> -->




							</tr>
						</thead>
						<tbody>
							<?php



							echo '<tr>
							<th scope="row">'.$id.'</th>
							<td>'.$nama.'</td>
							<td>'.$alamat.'</td>
							<td>'.$keluhan.'</td>
							<td>'.$diagnosa.'</td>
							<td>'.$obat.'</td>
							<td>'.$tanggal.'</td>



							</tr>';

						}
					}
					?>

        <!--   <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td colspan="2">Larry the Bird</td>
            <td>@twitter</td>
        </tr> -->
    </tbody>
</table>
</div>

<script>
	window.print();
</script>

</body>
</html>


