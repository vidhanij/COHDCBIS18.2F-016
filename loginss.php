<html >
<head>
<title>Login Form</title>
</head>
<body>
<form name="frmlogin" method="post" action="">
<table>
<tr>
<td>User Name :</td><td><input type="text" name="txtname"/></td> <br /><br />
<tr/>
<tr>
<td>Password :</td><td><input type="password" name="txtpassword"/> </td><br /><br />
</tr>
<tr><td></td>
<td><input type="submit" name="btnsubmit" value="LOGIN "/></td>
</tr>
</table>
</form>
</body>
</html>
<?php
session_start();
if(isset($_post["txtname"]))
{
	$uname=$_post["txtname"];
	$password=$_post["txtpassword"];
	if($uname=="cohdcbis" && $password=="cbis")
	{
		header("location: welcomess.php");
		$_session['lat']=time();
	}
}
?>



