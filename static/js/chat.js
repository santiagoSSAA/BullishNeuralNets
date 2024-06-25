// Function to fetch chat messages from Flask endpoint
async function fetchChatMessasges() {
    try {
        const response = await fetch('/get-messages');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const messages = await response.json();
        return messages;
    } catch (error) {
        console.error('Error fetching chat messages:', error);
        return [];
    }
}

// Function to render chat messages in the UI
async function renderChatMessages() {
    const chatMessagesContainer = document.getElementById('chatMessages');
    const messages = await fetchChatMessasges();
    chatMessagesContainer.innerHTML = ''; // Clear previous messages
    messages.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('d-flex', 'flex-row', 'justify-content-start', 'mb-4');
        messageDiv.innerHTML = `
        <img src="${message.avatar}" alt="avatar" style="width: 45px; height: 100%;">
        <div class="p-3 ms-3" style="border-radius: 15px; background-color: rgba(57, 192, 237, .2);">
          <p class="small mb-0">${message.text}</p>
        </div>
      `;
      chatMessagesContainer.appendChild(messageDiv);
    });
}

// Function to send a new message to Flask endpoint
async function sendMessage() {
    const message = document.getElementById('textAreaExample').value;
    if (message.trim() === '') return;

    try {
        const response = await fetch('/send-message', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ text: message }) // Adjust as per your backend's API
        });

        if (!response.ok) {
            throw new Error('Error sending message');
        }
        // Clear input after sending message
        document.getElementById('textAreaExample').value = '';

        // Refresh messages after sending
        await renderChatMessages();
    } catch (error) {
        console.error('Error sending message:', error);
    }
}

renderChatMessages();