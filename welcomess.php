<?php
session_start();
$time=$_server['request_time'];
$timeout_duration=10;
if(isset($_session['lat']) &&($time - $_session['lat'])>$timeout_duration)
{
  session_unset();
  session_destroy();
  session_start();
  header("location: loginss.php");
  exit();	
}
elseif($_session['lat'])
{
  echo("Welcome to HDCBIS page");	
}
else
{
	header("location: loginss.php");
}
?>

