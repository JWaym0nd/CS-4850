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

body {
    background-image: url('files/imgs/bg.jpg');
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: 1500px 1000px;
    }
</style>
</head>



<body>


<div>


<div class="title">
    SMART CHOICE
</div>
<div class="spacing"></div>
<div class="description1">
    &nbsp;&nbsp;&nbsp;&nbsp;Our product is a website which extensively compares and analyzes food delivery fees from the top 3 online
    food websites which are GrubHub, UberEats, and Postmates and &nbsp;&nbsp;&nbsp;&nbsp;gives the best option for customers for their
    satisfaction.

</div>
<div class="spacing"></div>
<div class="description2">
    This encapsulates the idea of the Internet of Things in smart retail because we are building a technology
    service that helps users get the best food delivery deals in a trillion dollar industry by
    improving user experience as well as saving time, energy, and costs in this busy world.<br>

</div>
<div class="double_spacing"></div>
    <!--
    <div class="icon-bar">


        <a href="https://www.grubhub.com/"><img src="files/imgs/grubhub.png" align="left" width="150" height="100"></a>
        <a href="https://www.ubereats.com/"><img src="files/imgs/ubereats.jpg" align="left" width="150" height="100"></a>
        <a href="https://postmates.com/"><img src="files/imgs/postmates--.png" align="left" width="150" height="100"></a>

    </div>
    -->

    <div class="part2">

        <div class="bg-logo">
            <img src="files/imgs/smart_choice.png" width="230" height="183" alt="">
        </div>


        <div id="header">

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
        

	<script src='javascript/script.js'></script>
</body>


</html>
