document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("topics-list");
    const searchBox = document.getElementById("searchBox");

    if (!sidebar) {
        console.error("Sidebar element not found!");
        return;
    }

    let allTopics = [];

    // Adjust JSON path based on file location
    let jsonPath = window.location.pathname.includes("/topics/") ? "../dsa.json" : "dsa.json";

    console.log("Fetching JSON from:", jsonPath); // Debugging

    // Fetch DSA Topics from JSON
    fetch(jsonPath)
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to load JSON");
            }
            return response.json();
        })
        .then(data => {
            allTopics = data.DSA;
            displayTopics(allTopics);
        })
        .catch(error => console.error("Error loading topics:", error));

    // Function to Display Topics in Sidebar
    function displayTopics(topics) {
        sidebar.innerHTML = "";
        topics.forEach(topic => {
            let li = document.createElement("li");
            li.className = "list-group-item list-group-item-action";

            // Ensure "topics/" is always present in the link
            let topicLink = topic.link.startsWith("topics/") ? topic.link : `topics/${topic.link}`;

            li.innerHTML = `<a href="${topicLink}" class="topic-link">${topic.name}</a>`;
            sidebar.appendChild(li);
        });
    }

    // Search Topics
    if (searchBox) {
        searchBox.addEventListener("input", function () {
            const searchText = this.value.toLowerCase();
            const filteredTopics = allTopics.filter(topic => 
                topic.name.toLowerCase().includes(searchText)
            );
            displayTopics(filteredTopics);
        });
    }
});
