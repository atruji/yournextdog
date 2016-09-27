<!DOCTYPE html>
<html lang="en">
<div id="loader-bkgd"></div>
<div id="loading"></div>
<div id="content">
<head>
    <?php 
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ip=$_SERVER['HTTP_CLIENT_IP'];}
    elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip=$_SERVER['HTTP_X_FORWARDED_FOR'];} else {
    $ip=$_SERVER['REMOTE_ADDR'];}
    ?>


<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-84784449-1', 'auto');
  ga('send', 'pageview', {
      'dimension1':  '<?php echo $ip; ?>'});

    </script>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="Description" content="Search for an adoptable dog in a whole new way!">
    <meta name="keywords" content="Dog Adoption, Image Search, Pets, Dog Rescue">
    <meta name="robots" content="noindex,nofollow">

    <title>YourNextDog</title>

    <link rel="shortcut icon" href="../static/assets/images/favicons/favicon.ico" />
    <link rel="apple-touch-icon" sizes="57x57" href="../static/assets/images/favicons/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="../static/assets/images/favicons/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="../static/assets/images/favicons/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="../static/assets/images/favicons/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="../static/assets/images/favicons/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="../static/assets/images/favicons/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="../static/assets/images/favicons/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="../static/assets/images/favicons/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../static/assets/images/favicons/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192"  href="../static/assets/images/favicons/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="../static/assets/images/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="../static/assets/images/favicons/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="../static/assets/images/favicons/favicon-16x16.png">
    <link rel="manifest" href="../static/assets/images/favicons/manifest.json">
    <meta name="msapplication-TileColor" content="#000000">
    <meta name="msapplication-TileImage" content="../static/assets/images/favicons/ms-icon-144x144.png">
    <meta name="theme-color" content="#000000">


    <!-- css -->
    <link rel="stylesheet" href="../static/assets/lib/bootstrap/dist/css/bootstrap.css">
    <link rel="stylesheet" href="../static/assets/lib/fontawesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="../static/assets/lib/ionicons/css/ionicons.css">
    <link rel="stylesheet" href="../static/assets/lib/owlcarousel/owl-carousel/owl.carousel.css">
    <link rel="stylesheet" href="../static/assets/lib/owlcarousel/owl-carousel/owl.theme.css">
    <link rel="stylesheet" href="../static/assets/lib/FlexSlider/flexslider.css">
    <link rel="stylesheet" href="../static/assets/lib/magnific-popup/dist/magnific-popup.css"/>

    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Raleway:100,300,400">
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:100,300,400">

    <link rel="stylesheet" href="../static/assets/css/main.css">
    <link rel="stylesheet" href="../static/assets/css/ie_fix.css">

    <script src="../static/assets/lib/components-modernizr/modernizr.js"></script>
    <script src="../static/assets/lib/jquery/dist/jquery.js"></script>
    <script src="../static/assets/lib/bootstrap/dist/js/bootstrap.js"></script>

</head>

<body data-spy="scroll" data-target="#main-nav-collapse" data-offset="100">

<?php $test="test" ?>

<div class="page-loader">
    <div class="loader">Loading...</div>
</div>
<!-- Fixed Top Navigation -->
<nav id="fixedTopNav" class="navbar navbar-fixed-top main-navigation" itemscope itemtype="https://schema.org/SiteNavigationElement" role="navigation">
    <div class="container">

        <div class="navbar-header">

            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#main-nav-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="ion-drag"></span>
            </button>

            <!-- Logo -->
            <div class="navbar-brand" itemscope itemtype="https://schema.org/Organization">
                <span itemprop="name" class="sr-only">YourNextDog.com</span>
                <a itemprop="url" href="/"><img src="../static/doggroup.png" alt="Dog Pack" height="75" width="90">
                    YourNextDog.com
                </a>
            </div>
            <!-- /Logo -->

        </div><!-- /.navbar-header -->

        <!-- Navigation Links -->
        <div class="collapse navbar-collapse" id="main-nav-collapse">
            <ul class="nav navbar-nav navbar-right">
                
                <li><a href="#services" itemprop="url">
                    <span itemprop="name">Find A Dog</span>
                </a></li>

                <li><a href="#footer-widgets" itemprop="url">
                    <span itemprop="name">About</span>
                </a></li>

                <li><a href="#footer-widgets" itemprop="url">
                    <span itemprop="name">Contact</span>
                </a></li>

            </ul>
        </div>
        <!-- /Navigation Links -->

    </div><!-- /.container -->
</nav>
<!-- /Fixed Top Navigation -->


    <!-- Header -->
    <header id="header" class="header-wrapper home-parallax home-fade dark-bg">
        <div class="color-overlay"></div>
        
        <div class="header-wrapper-inner">
            <div class="container">

                <div class="intro">
                    <h2>Looking to Adopt a New Best Friend?<p><?php echo $test; ?></p></h2>
                    <br><p>Search in a whole new way!<p>
                </div><!-- /.intro -->


                 <div style="color: rgba(255, 255, 255, 0.75); display: inline-block;">

                  
                  <p style="border-style: dashed; text-align:left;border-width: 1px;padding: .457em;">With YourNextDog.com you can get<br>recommendations for adoptable dogs<br>
                    in your area by showing us examples<br> of dogs you like.<br></p>
                    </div><br><br>
                    
                <a href="#services" class="btn btn-default-o onPageNav">Let's Go!</a>

            </div><!-- /.container -->


        </div>
        <!--<div class="overlay_vid"></div>
        <div id="videoBackground"
         class="overlay"
         data-property="{
                        poster: '../static/doggroup.png',
                        videoURL:'https://www.youtube.com/watch?v=s9UFV8I-QEQ',
                        containment:'.header-wrapper',
                        mute:true,
                        autoPlay:true,
                        loop:false,
                        opacity:1,
                        showControls:false,
                        showYTLogo:false}"></div>-->
        <!-- /.header-wrapper-inner -->
        <div class="overlay_vid"></div>
        <div class="fullscreen-bg">
        <video muted autoplay poster="../static/scene00001.jpg" class="fullscreen-bg__video">
            <source src="https://s3.amazonaws.com/akiajrrhy72f4guygb7-1/banner.mp4" type="video/mp4">
        </video>
    </header>
    <!-- /Header -->
    <!-- Service -->
    <section id="services" class="section services">
        <div class="container">

            <!---->
            <header class="section-heading">
                <h2>Let's Get Started!</h2>
            </header>
            <h4 class="text-center">How would you like to search?</h4>
            <p class"text-center" style="color: #000000; text-align:center;border-width: 1px;padding: .457em;">Show us dogs you like and we'll find you <br> adoptable dogs in your area that look similar.</p>
            <!---->

            <div class="section-content">
                <div class="row">
                    <div class="col-sm-4">

                        <!-- service -->
                        <div class="service">
                            <div class="about-service">
                                <p class="text-center"><img src="../static/discodog.gif" alt="Disco Dog" height="90" width="90"></p>
                                <h4 class="text-center">Upload a Photo</h4>
                                <p>Have a picture of a cute dog on your computer? Use the form below to upload it. Pictures can be in JPG, PNG or GIF formats and for best results, the size of the image should be at least 221 x 221.</p>
                            
                            </div>   
                            <form action="" method="post" name="searchfile" enctype="multipart/form-data" style="max-width: 90%;">
                            <p class="text-center">Please upload a dog image:<br>
                            {{ formfile.csrf_token }}
                            {{ formfile.fileName(size=40, style="max-width: 90%") }}<br></p>
                            <p>Please enter your zipcode:<br>
                            {{ formfile.zipcode(size=10) }}<br></p>
                            <p>
                            Search Radius?{{ formfile.radius }}
                            </p>
                            <p class="text-center"><input type="submit" name="btn" value="Search" style="font-face: 'Comic Sans MS'; font-size: larger; background-color:#a9a9a9" onclick="loading();"></p></form><h5 class="text-center">{{ errFile }}</h5>
                        <br></div>

                    </div>
                    <!-- col-sm-4 -->

                    <div class="col-sm-4">

                        <!-- service -->
                        
                        <div class="service">
                            <div class="about-service">
                                <p class="text-center"><img src="../static/boxerdog.gif" alt="Boxer Dog" height="90" width="90"></p>
                                <h4 class="text-center">Submit an Image Link</h4>
                                <p>
                                    The internet is basically just one big collage of cute dog pictures. Find a picture that you like, snatch the url and put it below. Hint: Right click on the image you find and select "Copy Image URL".
                                </p>

                            

                            </div>
                            <form action="" method="post" name="searchweb" enctype="multipart/form-data" style="max-width: 90%;">
                            <p class="text-center">Please enter a URL to a dog image:<br>
                            {{ formweb.csrf_token }}
                            {{ formweb.dogurl(size=40, style="max-width: 90%") }}<br></p><br>
                            <p>Please enter your zipcode:<br>
                            {{ formweb.zipcode(size=10) }}<br></p>
                            <p>
                            Search Radius?{{ formweb.radius }}
                            </p>
                            <p class="text-center"><input type="submit" value="Search" style="font-face: 'Comic Sans MS'; font-size: larger; background-color:#a9a9a9" onclick="loading();"></p></form><h5 class="text-center">{{ errWeb }}</h5>
                        </div>



                    </div><!-- col-sm-4 -->

                    <div class="col-sm-4">

                        <!-- service -->
                        <div class="service">
                            <div class="about-service">
                                <p class="text-center"><img src="../static/labdog.gif" alt="Labrador Dog" height="90" width="90"></p>
                                <h4 class="text-center">Interactive Matcher</h4>
                                <p><img src="../static/dogtinder.png" alt="Disco Dog" height="150" width="90" style="float: right; margin: 3px;">
                                    Don't have an picture in mind? Use the Interactive Matcher to get recommendations. You'll be shown a series of pictures and all you have to do is let  us know if you like or dislike the doggy in the picture. When you like at least 20 dogs we'll give you recommendations for dogs in your area that we think you'll love. 
                                <br>
                                </p><br><br><br><br><br><h4 class="text-center">COMING SOON...</h4><br><br>
                            </div>
                        </div>

                    </div><!-- col-sm-4 -->
                </div><!-- row -->
            </div><!-- section-content -->
        </div><!-- container -->
    </section>
    <!-- Service -->    

    <!-- Footer widgets -->
    <section id="footer-widgets" class="section footer-widgets dark-bg">
        <div style="margin: 0 auto">
        <div class="container">
            <div class="row">
                <div class="col-md-3 col-sm-6">
                    <div class="content-wrap widget-text">
                        <h4>About YourNextDog.com</h4>
                        <p>YourNextDog.com utilizes machine learning and the Petfinder API to help people find adoptable dogs in their areas. Site and match engine built by Andrew Trujillo, a Data Scientist currently looking for new projects. Contact Andrew with the info on the right. Thanks for visiting the site!</p>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="content-wrap widget-contact">
                        <h4>Contact info</h4>
                        <ul>
                            <li>
                                <i class="ion-home"></i> 3649 Market St, San Francisco, CA 94131
                            </li>
                            <li>
                                <i class="ion-android-call"></i> (505) 288-8342
                            </li>
                            <li>
                                <i class="ion-email"></i> contact@andrewdata.ninja
                            </li>
                            <li>
                                <i class="ion-social-github"></i> <a href='http://www.github.com/atruji'> github.com/atruji</a>
                            </li>
                            <li>
                                <i class="ion-social-linkedin"></i><a href='https://www.linkedin.com/in/andrewtrujillo'>linkedin.com/in/andrewtrujillo</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </section>
    <!-- Footer widgets -->
    <!-- footer -->
    <footer id="footer" class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-3 col-sm-4">
                    <p class="copyright text-xs-center">&copy; 2015 YourNextDog.com</p>
                </div>
            </div>
        </div>
    </footer>
</div>
<!-- #footer -->

<a id="totop" href="#totop"><i class="fa fa-angle-double-up"></i></a>
<!-- js -->
<script src="../static/assets/lib/imagesloaded/imagesloaded.pkgd.min.js"></script>
<script src="../static/assets/lib/isotope/dist/isotope.pkgd.min.js"></script>
<script src="../static/assets/lib/owlcarousel/owl-carousel/owl.carousel.js"></script>
<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
<script src="../static/assets/lib/waypoints/lib/jquery.waypoints.min.js"></script>
<script src="../static/assets/lib/waypoints/lib/shortcuts/inview.min.js"></script>

<script src="../static/assets/lib/FlexSlider/jquery.flexslider.js"></script>
<script src="../static/assets/lib/simple-text-rotator/jquery.simple-text-rotator.js"></script>
<script src="../static/assets/lib/jquery.mb.YTPlayer/dist/jquery.mb.YTPlayer.min.js"></script>
<script src="../static/assets/lib/magnific-popup/dist/jquery.magnific-popup.js"></script>

<script src="../static/assets/js/main.js"></script>

<script type="text/javascript">// <![CDATA[
        function loading(){
            $("#loading").show();
            $("#content").hide();     
        }
// ]]></script>

<script type="text/javascript">
        var switch_sect = '{{switcher}}';
        if (switch_sect == 'true') {
            window.location.replace("#services");

        }
</script>

<!--[if lt IE 10]>
<script>
    $('input, textarea').placeholder();
</script>
<![endif]-->

</body>
</html>
