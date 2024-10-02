$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    var Base_Exp = $("#Base_Exp").val();//Type
    var Attack = $("#Attack").val();
    var Sp_Atk = $("#Sp_Atk").val();
    var Defense = $("#Defense").val();
    var Sp_Def = $("#Sp_Def").val();
    var Growth_Rate = $("#Growth_Rate").val();
    var HP = $("#HP").val();


    // check if inputs are valid

    // create the payload
    var payload = {
        "Base_Exp": Base_Exp,
        "Attack": Attack,
        "Sp_Atk": Sp_Atk,
        "Defense": Defense,
        "Sp_Def": Sp_Def,
        "Growth_Rate": Growth_Rate,
        "HP": HP
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            var prob = parseFloat(returnedData["prediction"]);

            if (prob > 0.5) {
                $("#output").text(`You Survived with probability ${prob}!`);
            } else {
                $("#output").text(`You did not survive with probability ${prob}, sorry. :(`);
            }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}

// script.js
const slider1 = document.getElementById('slider1');
const slider2 = document.getElementById('slider2');
const rangeDisplay = document.getElementById('range-display');
const sliderRange = document.getElementById('slider-range');

function updateSliderRange() {
    const minVal = parseInt(slider1.value);
    const maxVal = parseInt(slider2.value);

    // Ensure slider1 is always less than slider2
    if (minVal > maxVal) {
        slider1.value = maxVal;
    }

    // Update the display text
    rangeDisplay.textContent = `${slider1.value} - ${slider2.value}`;

    // Set the width and position of the slider range
    const percent1 = (minVal / slider1.max) * 100;
    const percent2 = (maxVal / slider2.max) * 100;
    sliderRange.style.left = `${percent1}%`;
    sliderRange.style.width = `${percent2 - percent1}%`;
}

// Event listeners for both sliders
slider1.addEventListener('input', updateSliderRange);
slider2.addEventListener('input', updateSliderRange);

// Initialize the display
updateSliderRange();
