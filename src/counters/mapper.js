function mapper() {
  emit(this.counter_id, {
    id: this.counter_id,
    installed_at: this.installed_at,
    park_code: this.park_code,
    cord_north: this.cord_north,
    cord_east: this.cord_east,
    visits: this.visits,
  });
}
