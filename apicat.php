<!doctype html>
<html>
    <head>
       <title>Carrier has arrived</title>
    </head>
  <h3></h3>
</html>

<?php
getSslPage();


function getSslPage($url) {    
    $url = "https://www.facebook.com";    
    $url = "https://www.google.com";
    
    $ch = curl_init();
    echo 'Fetching' + $url +'\n';
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_HEADER, FALSE);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_REFERER, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
    
    $result = curl_exec($ch);
    curl_close($ch);
    echo $result;
}

?>
