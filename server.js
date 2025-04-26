

const express = require("express");
const axios = require("axios");
const cors = require("cors");
const path = require("path");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

// Serve static files (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, "try.html")));

// API Route to Fetch Jobs
const GOOGLE_CLOUD_PROJECT_ID = "free-job-link-449610";
const API_URL = `https://cloud-talent.googleapis.com/v4/projects/${GOOGLE_CLOUD_PROJECT_ID}/jobs:search`;

app.post("/search-jobs", async (req, res) => {
    try {
        const response = await axios.post(API_URL, req.body, {
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${process.env.e3d3a3f11bf38d72e780d0d2eb5aacfda3052878}`
            }
        });
        res.json(response.data);
    } catch (error) {
        console.error("Error fetching jobs:", error);
        res.status(500).json({ error: "Failed to fetch jobs" });
    }
});

// Root Route to Serve HTML File
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "try.html"));
});

// Start the Server
app.listen(3000, () => console.log("Server running on http://127.0.0.1:3000"));
