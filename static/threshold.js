import cv2
import numpy as np
import matplotlib.pyplot as plt

function threshold()
{
  var canv2 = document.getElementById("Q2");
  var context2 = canv2.getContext("2d");
  var originalImagedata = context2.getImageData(0, 0, canv2.width, canv2.height);
  var binaryImageData = context2.getImageData(0, 0, canv2.width, canv2.height);

  console.log(binaryImageData);


  var red_lo = document.getElementById("S1").value;
  var red_hi = document.getElementById("S2").value;
  var blue_lo = document.getElementById("S3").value;
  var blue_hi = document.getElementById("S4").value;
  var green_lo = document.getElementById("S5").value;
  var green_hi = document.getElementById("S6").value;

  // var red_hi = 255;
  // var blue_lo = 0;
  // var blue_hi = 255;
  // var green_lo = 0;
  // var green_hi = 255;

  var i;
  for (i = 0; i < originalImagedata.data.length; i += 4) 
  {
    // if(originalImagedata.data[i] < red_lo ) originalImagedata.data[i] = 0;
    // if(originalImagedata.data[i] > red_hi ) originalImagedata.data[i] = 0;
    // if(originalImagedata.data[i+1] < blue_lo ) originalImagedata.data[i+1] = 0;
    // if(originalImagedata.data[i+1] > blue_hi ) originalImagedata.data[i+1] = 0;
    // if(originalImagedata.data[i+2] < green_lo ) originalImagedata.data[i+2] = 0;
    // if(originalImagedata.data[i+2] > green_hi ) originalImagedata.data[i+2] = 0;

    if( (originalImagedata.data[i] < red_lo) || (originalImagedata.data[i] > red_hi) || (originalImagedata.data[i+1] < blue_lo) || (originalImagedata.data[i+1] > blue_hi ) 
      || (originalImagedata.data[i+2] < green_lo ) || (originalImagedata.data[i+2] > green_hi) )
    {
      // originalImagedata.data[i] = 0;
      // originalImagedata.data[i+1] = 0;
      // originalImagedata.data[i+2] = 0;
      binaryImageData.data[i] = 255;
      binaryImageData.data[i+1] = 255;
      binaryImageData.data[i+2] = 255;
      binaryImageData.data[i+3] = 255;


    }
    else 
    {
      binaryImageData.data[i] = 0;
      binaryImageData.data[i+1] = 0;
      binaryImageData.data[i+2] = 0;
      binaryImageData.data[i+3] = 0;
    }
  }

  // var canv1 = document.getElementById("Q1");
  // var context1 = canv1.getContext("2d");

  // context1.putImageData(originalImagedata, 0, 0);


  var canv3 = document.getElementById("Q3");
  var context3 = canv3.getContext("2d");

  context3.putImageData(binaryImageData, 0, 0);
  // alert("Done Threshold function");

  // alert("Done Threshold function");

}

window.onload = function() 
{
   var S1 = document.getElementById("S1");

   S1.oninput = function()
   {
    threshold();

};

