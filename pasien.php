<!-- import modul connect.php  -->
<?php
  include "connect.php";
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
      <button type="submit" class="btn btn-primary my-5">
        <a href="add_pasien.php" class="text-light">Add Patient</a>
      </button>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">id</th>
            <th scope="col">NIK</th>
            <th scope="col">Name</th>
            <th scope="col">Mobile</th>
            <th scope="col">Gender</th>
            <th scope="col">Operations</th>


          </tr>
        </thead>
        <tbody>
          <?php

            $sel_pasien = "select id_pasien,nik,nama_pasien,no_telp,j_kelamin from pasien";
            $result = mysqli_query($con,$sel_pasien);
            if($result){
              while($row = mysqli_fetch_assoc($result)){ 
                $id = $row['id_pasien'];
                $NIK = $row['nik'];
                $nama = $row['nama_pasien'];
                $no_telp = $row['no_telp'];
                $jk = $row['j_kelamin'];
                echo '<tr>
                  <th scope="row">'.$id.'</th>
                  <td>'.$NIK.'</td>
                  <td>'.$nama.'</td>
                  <td>'.$no_telp.'</td>
                  <td>'.$jk.'</td>
                  <td>
                    <button type="submit" class="btn btn-primary ">
                      <a href="upd_pasien.php?upd_id='.$id.'" class="text-light">Update</a>
                    </button>
                    <button type="submit" class="btn btn-danger ">
                      <a href="del_pasien.php?del_id='.$id.'" class="text-light">Delete</a>
                    </button>
                  </td>

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

  </body>
  </html>

