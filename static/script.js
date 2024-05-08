const checkInDate = document.getElementById("checkin")
const checkOutDate = document.getElementById("checkout")


checkOutDate.addEventListener("change", validateDate);

function validateDate() {
    const checkIn = new Date(checkInDate.value);
    const checkOut = new Date(checkOutDate.value);

    if (checkOut <= checkIn) {
        alert("Check out date should be later than the check in date");
        checkOutDate.value = "";
    }
}