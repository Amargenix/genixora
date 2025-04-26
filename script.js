document.addEventListener("DOMContentLoaded", function () {
    fetch("/categories.json")
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("topics-list");
            list.innerHTML = ""; // Clear existing content

            data.categories.forEach(topic => {
                let col = document.createElement("div");
                col.className = "col-md-4 my-2";

                let card = document.createElement("div");
                card.className = "card p-3 shadow-sm";
                card.innerHTML = `
                    <h5 class="card-title">${topic.name}</h5>
                    <a href="${topic.file}" class="btn btn-primary">Learn More</a>
                `;

                col.appendChild(card);
                list.appendChild(col);
            });

            // Search functionality
            document.getElementById("searchBox").addEventListener("input", function () {
                const searchText = this.value.toLowerCase();
                list.innerHTML = ""; // Clear existing content

                data.categories
                    .filter(topic => topic.name.toLowerCase().includes(searchText))
                    .forEach(topic => {
                        let col = document.createElement("div");
                        col.className = "col-md-4 my-2";

                        let card = document.createElement("div");
                        card.className = "card p-3 shadow-sm";
                        card.innerHTML = `
                            <h5 class="card-title">${topic.name}</h5>
                            <a href="${topic.file}" class="btn btn-primary">Learn More</a>
                        `;

                        col.appendChild(card);
                        list.appendChild(col);
                    });
            });
        })
        .catch(error => console.error("Error loading topics:", error));
});
