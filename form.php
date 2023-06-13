<?php
    $email_admin="leoberton79@gmail.com";
    $object="Contact via le site";

    $_POST["send"];

    if(isset($_POST["send"]) && !empty($_POST["send"]))(
        if(isset($_POST["name"]) && !empty($_POST["name"]) && isset($_POST["email"]) && !empty($_POST["email"]) && isset($_POST["message"]) && !empty($_POST["message"]))(
            
            $message=$_POST["message"]
            $header ="From: " . $_POST["email"] . "\r\n" ;

            if (mail($email_admin,$object,$message,$header))
            (
                return header("location:index.html");
            )
        )
    
        )


?>