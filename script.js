// Add JavaScript code to add interactivity or dynamic behavior to your Valentine's Day card

// Wait for the DOM content to be loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the envelope element
    var envelope = document.querySelector('.envelope');

    // Add click event listener to toggle open/close effect
    envelope.addEventListener('click', function() {
        // Toggle class to open/close envelope
        envelope.classList.toggle('open');
    });
});