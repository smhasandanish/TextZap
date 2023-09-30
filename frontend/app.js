document.addEventListener('DOMContentLoaded', function () {
    const inputText = document.getElementById('inputText');
    const summarizeButton = document.getElementById('summarizeButton');
    const summaryText = document.getElementById('summaryText');

    summarizeButton.addEventListener('click', function () {
        const textToSummarize = inputText.value;

        // Check if the input text is empty
        if (!textToSummarize.trim()) {
            alert('Please enter text to summarize.');
            return;
        }

        // Make a POST request to your backend API
        fetch('https://smhasandanish.pythonanywhere.com/api/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: textToSummarize }),
        })
            .then((response) => response.json())
            .then((data) => {
                // Display the summary returned by the backend
                summaryText.textContent = data.summary;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });
});
