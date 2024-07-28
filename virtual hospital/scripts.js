document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Simple client-side validation
    if (!username || !password) {
        displayErrorMessage('Please fill in both fields.');
        return;
    }

    // Simulate a server request
    const isValidUser = mockServerValidation(username, password);

    if (isValidUser) {
        alert('Login successful!');
        // Redirect to dashboard or home page
        window.location.href = 'dashboard.html';
    } else {
        displayErrorMessage('Invalid username or password.');
    }
});

function displayErrorMessage(message) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.textContent = message;
}

function mockServerValidation(username, password) {
    // Mock validation - in real scenario, perform server-side validation
    const validUsername = 'user';
    const validPassword = 'pass';
    
    return username === validUsername && password === validPassword;
}
