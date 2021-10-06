<!DOCTYPE html>
<html>
  <head>
    <title>LibreDay</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  </head>
  <body>
    <header class="w3-container w3-teal">
      <h1>LibreDay</h1>
      <h3>Open source version of WorkDay (parody purposes only)</h3>
    </header>
    <div class="w3-center">
      <div class="w3-container w3-half w3-margin-top">
        <?php
          file_put_contents("/input.txt", $_POST["sid"]);
        ?>
        <p>View generated schedule <a href="/pre-compiled-calendar.png">here</a></p>
        <p><b>Please wait 5 seconds for schedule to load</b></p>
      </div>
    </div>
    <p><i>Many eyes make all bugs shallow.</i></p>
  </body>
</html>
