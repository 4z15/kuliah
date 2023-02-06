<?php  
include "connect.php";

session_start();
 
// if (isset($_SESSION['username'])) {
//     header("Location:index.php");
// }
 
if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = ($_POST['password']);
 
    $sql = "SELECT username,password FROM user ";
    $result = mysqli_query($con, $sql);
    if ($result) {
        $row = mysqli_fetch_assoc($result);
        if (($username == $row['username'] ) && ($password == $row['password'])) {
          // code...
            $_SESSION['username'] = $row['username'];
        // header("Location:index.php");
            echo "
            <script>
              alert('Berhasil Login sebagai admin');
            document.location.href='index.php'; 

            </script> 
            ";
        }
      
    } 
    else 
    {
        echo "<script>
        alert('username atau password Anda salah. Silahkan coba lagi!');
        </script>";
    }
}




?>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="css/style.css">
<title> E_Puskesmas-Login </title>
</head>
<body>
  <body>
    <div class="login-page">
      <div class="form">
        <div class="login">
          <div class="login-header">
            <h3>E_PUSKESMAS</h3>
            <p>Login</p>
          </div>
        </div>
        <form class="login-form" method="POST">
          <input type="text" placeholder="username" name="username" />
          <input type="password" placeholder="password" name="password" />
          <button name = "submit" >
          <!-- <a href="index.php" class="">Login</a> -->
          Login
        </button>
        </form>
      </div>
    </div>
</body>
</body>
</html>