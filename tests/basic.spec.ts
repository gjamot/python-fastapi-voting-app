import { test, expect } from '@playwright/test';

test('loads post data from API', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('h1')).toHaveText('React JS | Python Fast API Voting APP');
  await expect(page.locator('pre')).toContainText('"title"');
});