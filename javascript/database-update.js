const { Client } = require("@notionhq/client")
const dotenv = require("dotenv")

dotenv.config()

const databaseId = process.env.NOTION_DATABASE_ID
const notion = new Client({ auth: process.env.NOTION_KEY })

console.log(databaseId,process.env.NOTION_KEY ,  notion);


/**
 * Gets tasks from the database.
 *
 * @returns {Promise<Array<{ pageId: string, status: string, title: string }>>}
 */

async function getTasksFromNotionDatabase() {
  const pages = []
  let cursor = undefined

  while (true) {
    const { results, next_cursor } = await notion.databases.query({
      database_id: databaseId,
      start_cursor: cursor,
    })
    pages.push(...results)
    if (!next_cursor) {
      break
    }
    cursor = next_cursor
  }
  console.log(`${pages.length} pages successfully fetched.`)

  const tasks = []
  for (const page of pages) {
    const pageId = page.id

    const statusPropertyId = page.properties["Status"].id
    const statusPropertyItem = await getPropertyValue({
      pageId,
      propertyId: statusPropertyId,
    })
    const status = statusPropertyItem.select
      ? statusPropertyItem.select.name
      : "No Status"

    const titlePropertyId = page.properties["Name"].id
    const titlePropertyItems = await getPropertyValue({
      pageId,
      propertyId: titlePropertyId,
    })
    const title = titlePropertyItems
      .map(propertyItem => propertyItem.title.plain_text)
      .join("")

    tasks.push({ pageId, status, title })
  }

  return tasks
}

async function findAndSendEmailsForUpdatedTasks() {
  console.log("\nFetching tasks from Notion DB...")
  let cursor = undefined
  const { results, next_cursor } = await notion.databases.query({
    database_id: "79b834ecd40e4866907799ce7f7b0028",
    // start_cursor: cursor,
  })

  // const currentTasks = await getTasksFromNotionDatabase()
  // console.log('currentTasks', currentTasks);
}

findAndSendEmailsForUpdatedTasks();

// /**
//  * Initialize local data store.
//  * Then poll for changes every 5 seconds (5000 milliseconds).
//  */
// setInitialTaskPageIdToStatusMap().then(() => {
//   setInterval(findAndSendEmailsForUpdatedTasks, 5000)
// })

// /**
//  * Get and set the initial data store with tasks currently in the database.
//  */
// async function setInitialTaskPageIdToStatusMap() {
//   const currentTasks = await getTasksFromNotionDatabase()
//   for (const { pageId, status } of currentTasks) {
//     taskPageIdToStatusMap[pageId] = status
//   }
// }

