async function generateResearch() {

    const country = document.getElementById("country").value;
    const committee = document.getElementById("committee").value;

    const response = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            country: country,
            committee: committee
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText = data.response;
}
