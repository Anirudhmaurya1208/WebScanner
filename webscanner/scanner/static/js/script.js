// document.addEventListener("DOMContentLoaded", function() {
//     const scanButton = document.getElementById("scanButton");
//     const urlInput = document.getElementById("urlInput");
//     const resultContainer = document.getElementById("resultContainer");

//     scanButton.addEventListener("click", function() {
//         const url = urlInput.value.trim();
//         if (url === "") {
//             alert("Please enter a URL to scan.");
//             return;
//         }

//         resultContainer.innerHTML = "Scanning...";
        
//         fetch("/api/scan/", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({ url: url })
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 resultContainer.innerHTML = `<p>Scan Complete:</p><pre>${JSON.stringify(data.result, null, 2)}</pre>`;
//             } else {
//                 resultContainer.innerHTML = "Error: " + data.error;
//             }
//         })
//         .catch(error => {
//             resultContainer.innerHTML = "An error occurred. Please try again.";
//             console.error("Error:", error);
//         });
//     });
// });
$(document).ready(function () {
    $("form").submit(function (event) {
        event.preventDefault(); // Prevent page reload

        let url = $("input[name='url']").val();
        let csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $("#scan-result").remove(); // Remove previous results
        $("form").after('<p id="loading" style="font-weight:bold;">🔍 Scanning...</p>');

        $.ajax({
            type: "POST",
            url: "/scan/", // Update if needed
            data: { url: url, csrfmiddlewaretoken: csrfToken },
            success: function (response) {
                $("#loading").remove();
                
                // Define colors and icons based on status
                let statusColor, statusIcon;
                if (response.status === "Safe") {
                    statusColor = "green";
                    statusIcon = "✅";
                } else if (response.status === "Suspicious") {
                    statusColor = "orange";
                    statusIcon = "⚠️";
                } else {
                    statusColor = "red";
                    statusIcon = "❌";
                }

                let resultHtml = `
                    <section id="scan-result" class="result-card" style="border: 2px solid ${statusColor}; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); text-align: center; max-width: 600px; margin: 20px auto;">
                        <h2 style="color: ${statusColor};">${statusIcon} Scan Result</h2>
                        <p><strong>🔗 URL:</strong> <span style="word-wrap: break-word;">${response.url}</span></p>
                        <p><strong>📌 Status:</strong> <span style="color: ${statusColor}; font-weight: bold;">${response.status}</span></p>
                        <p><strong>📝 Details:</strong> ${response.details}</p>
                        <hr>
                        <h3>🔍 Additional Info</h3>
                        <p><strong>🌍 IP Address:</strong> ${response.ip}</p>
                        <p><strong>🔒 SSL Status:</strong> ${response.ssl_status}</p>
                        <p><strong>🏢 Domain Registrar:</strong> ${response.domain_info.Registrar}</p>
                        <p><strong>🌎 Country:</strong> ${response.domain_info.Country}</p>
                        <p><strong>📅 Creation Date:</strong> ${response.domain_info["Creation Date"]}</p>
                    </section>
                `;

                $("form").after(resultHtml);
            },
            error: function () {
                $("#loading").remove();
                $("form").after("<p style='color:red; font-weight: bold;'>❌ Error scanning URL. Please try again.</p>");
            }
        });
    });
});
