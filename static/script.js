const checkInDate = document.getElementById("checkin");
const checkOutDate = document.getElementById("checkout");

function validateInDate() {
    const checkIn = new Date(checkInDate.value);
    const today = new Date();

    if (checkIn <= today) {
        alert("Your check in date should be later than today");
        checkInDate.value= "";
    }
}

function validateOutDate() {
    const checkIn = new Date(checkInDate.value);
    const checkOut = new Date(checkOutDate.value);
 
    if (checkOut <= checkIn) {
        alert("Your check out date should be later than the check in date");
        checkOutDate.value = "";
    }
}

checkInDate.addEventListener("change", validateInDate);
checkOutDate.addEventListener("change", validateOutDate);

const commuteInput = document.getElementById("commuteInput");
const travelInput = document.getElementById("travelInput");
const travelRadios = document.querySelectorAll('input[name="travel"]').forEach((radio) => {
    radio.addEventListener("change", () => {
        if (radio.value === "commute") {
            commuteInput.required = true;
            travelInput.required = false;
        } else if (radio.value === "distance") {
            commuteInput.required = false;
            travelInput.required = true;
        }
    });
});

