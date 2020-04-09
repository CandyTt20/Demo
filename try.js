



async function main() {
  const stats = await axios(`https://api.todoist.com/sync/v8.3/completed/get_stats?token=${d9deec7ba39852d370168e80ebb66e4b60d927df}`);
  await updateGist(stats.data);
}

