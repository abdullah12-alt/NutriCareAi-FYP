document.addEventListener("DOMContentLoaded", function () {
    let bottom = document.querySelector(".bottom");
    let input = document.querySelector("#txt");
    let sendbtn = document.querySelector(".uil-message");
    let ul = document.querySelector("#list_cont");

    bottom.addEventListener("click", () => {
        input.focus();
    });

    input.addEventListener("input", () => {
        if (input.value.length > 0) {
            sendbtn.style.background = "#11ba91";
        } else {
            sendbtn.style.background = "transparent";
        }
    });

    function ChatGPT() {
        if (!input.value.trim()) {
            return; // If input is empty or contains only whitespace, do nothing
        }

        sendbtn.style.background = "transparent";
        let typingAnimationDiv = document.createElement("div");
        typingAnimationDiv.className = "typing-animation";
        for (let i = 0; i < 3; i++) {
            let dotSpan = document.createElement("span");
            dotSpan.className = "dot";
            typingAnimationDiv.appendChild(dotSpan);
        }
        let li2 = document.createElement("li");
        li2.className = "rchat";
        li2.appendChild(typingAnimationDiv);
        let li = document.createElement("li");
        li.className = "schat";
        li.textContent = input.value;
        ul.appendChild(li);
        setTimeout(() => {
            ul.appendChild(li2);
            $(".msgs_cont").scrollTop($(".msgs_cont")[0].scrollHeight);
        }, 500);
        sendbtn.disabled = true;
        $(".msgs_cont").scrollTop($(".msgs_cont")[0].scrollHeight);

        fetch('chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'user_input=' + encodeURIComponent(input.value),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            let i = 0;
            const intervalId = setInterval(() => {
                if (i < data.response.length) {
                    li2.textContent += data.response[i];
                    $(".msgs_cont").scrollTop($(".msgs_cont")[0].scrollHeight);
                    i++;
                } else {
                    clearInterval(intervalId);
                    sendbtn.disabled = false;
                }
            }, 20);
        })
        .catch(error => {
            console.error('Error:', error);
            li2.textContent = `Not working`;
            ul.appendChild(li2);
            $(".msgs_cont").scrollTop($(".msgs_cont")[0].scrollHeight);
        });
        
        input.value = ""; // Clear input field after sending message
    }

    sendbtn.addEventListener("click", ChatGPT);
});
