function mapper() {
  emit(`${this.counter_id}-${this.weekday}`, {
    id: this.counter_id,
    visits: this.visits,
    weekday: this.weekday,
  });
}
