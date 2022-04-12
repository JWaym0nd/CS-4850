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
    <style>
        .php-output1 {
            background-color: #FFA074;

        }

        .php-output2 {
            background-color: #ffe3ae;
            font-family: cursive;

        }
    </style>

</head>

<body>
<div id="header">
    <div class="bg-logo">
        <img src="files/imgs/smart_choice.png" width="230" height="183" alt="">
    </div>
    <div class="searchForm">
        <form class="searchRestaurantForm"  action="index-clone.php" method="post" >
            <input type="text" name="zipcode" id="zipcode" class="search-btn" value="" placeholder="Enter your address">
            <input type="text" name="restaurant" id="restaurant" class="search-btn" value="" placeholder="Enter the restuarant">
            <input type="text" name="item" id="item" class="search-btn" value="" placeholder="Enter the items to order">
            <br/>
            <input type="submit" class="search" name="Search" id="Search" value="Search" onclick="getLocation()" />
            <br/>
        </form>
        <span id="zipcodeerror"></span>
        <div id="latlong"></div>
    </div>
</div>



<div class="php-output1">
    <center>
Zipcode: <?php echo $_POST["zipcode"]; ?><br>
</center>
</div>


    <div class="php-output2">
        <center>
     <div class="php-output2">
        <center>
    <?php
    //take in the posted values 
    $address = "\"".$_POST['zipcode']."\"";
    $restaurant ="\"".$_POST['restaurant']."\"";
    //DEBUGGING CODE commented out
    //posted values sanity check
    //echo "posted address: $address<br>";
    //echo "posted restaurant: $restaurant<br>";
    //set up variables to store the output of the command
    $output = null;
    $retval = null;
    $command = escapeshellcmd("python3 ../scraper.py $address $restaurant");
    //echo "<br>Command executed: $command <br> ";      
    exec($command,$output,$retval);
    //echo "<br>Returned with: $retval<br> ";
    //echo var_dump($output); 



    echo"<h2>$output[0]:$output[1]</h2>";
    echo"<h2>$output[2]:$output[3]</h2>";
    echo"<h2>$output[4]:$output[5]</h2>";


    ?>

        </center>
    </div>



</div>
    <div class="icon-bar">


        <a href="https://www.grubhub.com/"><img src="files/imgs/grubhub.png" align="left" width="150" height="100"></a>
        <a href="https://www.ubereats.com/"><img src="files/imgs/ubereats.jpg" align="left" width="150" height="100"></a>
        <a href="https://postmates.com/"><img src="files/imgs/postmates.jpg" align="left" width="150" height="100"></a>

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


<script src='javascript/script.js'></script>

</body>
</html>
