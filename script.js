async function sendMessage() {
    const contact = document.getElementById("contact").value;
    const message = document.getElementById("message").value;
    const chat = document.getElementById("chat");

    chat.innerHTML += `<div><b>To ${contact}:</b> ${message}</div>`;

    const response = await fetch('https://your-hugging-face-space-url', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ contact: contact, message: message })
    });

    const data = await response.json();
    chat.innerHTML += `<div><b>Response:</b> ${data.response}</div>`;
    document.getElementById("message").value = "";
}
