<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="utf-8">
    <title>Smartchoice - The best food delivery option</title>
    <link rel="stylesheet" href="css/styles.css">
    <link href="images/favicon.ico" rel="shortcut icon"/>
    <!-- stylesheet Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Js Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>

    <!-- font awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>
<div id="header">
    <div class="bg-logo">
        <img src="files/imgs/smart_choice.png" width="337" alt="">
    </div>


Zipcode: <?php echo $_POST["zipcode"]; ?><br>
Restaurant: <?php echo $_POST["restaurant"]; ?><br>
Items:  <?php echo $_POST["item"]; ?>


</div>
    <div class="icon-bar">

        <a href="https://www.ubereats.com/"><img src="files/imgs/ubereats.jpg" align="left" width="100" height="70"></a>
        <a href="https://www.grubhub.com/"><img src="files/imgs/grubhub.png" align="left" width="100" height="70"></a>
        <a href="https://postmates.com/"><img src="files/imgs/postmates.jpg" align="left" width="100" height="70"></a>

    </div>



    <div id="feature-block">
        <div class="row feature-btn">
            <div class="col-md-4" onclick="showLocation()">
                <img class="img_location" src="files/imgs/location.png" alt="">
                <h2>Your Location</h2>
                <p>Select your location to find best prices</p>
                <span id="location" style="display: none;">New York, NYC, USA</span>
            </div>
            <div class="col-md-4" onclick="showRestaurant()">
                <img src="files/imgs/Storefront.png" alt="">
                <h2>Restaurant</h2>
                <p>Search and choose from our wide range of Restaurants</p>
                <span id="restaurant" style="display: none;">Available Restaurants are Crown Shy, Atoboy</span>
            </div>
            <div class="col-md-4" onclick="showOrder()">
                <img src="files/imgs/order.png" style="width: 154px; height: 154px;" alt="">
                <h2>Order</h2>
                <p>Make an order now!</p>
                <span id="order" style="display: none;">Order Online for Home Delivery</span>
            </div>
        </div>
    </div>
</div>

<?php

$csvData = file_get_contents("web-order.csv");
$lines = explode(PHP_EOL, $csvData);
$array = array();
foreach ($lines as $line) {
    $array[] = str_getcsv($line);
}
//  print_r($array);
print("\nLocation: ");
print_r($array[1][0]);
print("\nRestaurant: ");
print_r($array[1][1]);
print("\nDelivery fee: ");
print_r($array[1][2]);
?>
<script src='javascript/script.js'></script>

</body>
</html>
