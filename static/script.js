const checkInDate = document.getElementById("checkin");
const checkOutDate = document.getElementById("checkout");

checkInDate.addEventListener("change", validateInDate);
checkOutDate.addEventListener("change", validateOutDate);

function validateInDate() {
    console.log("Checking the checkin date");
    const checkIn = new Date(checkInDate.value);
    const today = new Date();

    if (checkIn < today) {
        alert("Your check in date should be later than today");
        checkInDate.value= "";
    }
}

function validateOutDate() {
    console.log("Checking the checkout date");
    const checkIn = new Date(checkInDate.value);
    const checkOut = new Date(checkOutDate.value);
 
    if (checkOut <= checkIn) {
        alert("Check out date should be later than the check in date");
        checkOutDate.value = "";
    }
}
