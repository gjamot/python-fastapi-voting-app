import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  timeout: 30_000,
  expect: {
    timeout: 5_000,
  },
  webServer: {
    command: "docker-compose up --build",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
  },
  use: {
    trace: "on",
  },
});
