<?php
$db = mysql_connect("localhost", "root");
if (!$db) {
    die("Could not connect");
}
if (!mysql_select_db("php_mysql_test")) {
    die("Could not select database");
}
$res = mysql_query("SELECT * from foobar");
$row = mysql_fetch_assoc($res);
printf("%s is %d\n", $row['name'], $row['value']);
?>
