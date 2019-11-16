function reducer(_, values) {
  function red(acc, item) {
    acc.visits += item.visits;
    delete item.visits
    return Object.assign(acc, item);
  }
  return values.reduce(red, { visits: 0 });
}
