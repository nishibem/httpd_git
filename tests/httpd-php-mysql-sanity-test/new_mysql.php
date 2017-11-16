<?php
$db = mysqli_connect("localhost", "root");
if (!$db) {
    die("Could not connect");
}
if (!mysqli_select_db($db, "php_mysql_test")) {
    die("Could not select database");
}
$res = mysqli_query($db, "SELECT * from foobar");
$row = mysqli_fetch_assoc($res);
printf("%s is %d\n", $row['name'], $row['value']);
?>
