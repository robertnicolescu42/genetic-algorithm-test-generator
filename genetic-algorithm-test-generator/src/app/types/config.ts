export class QuizConfig {
  GD: number;
  population_size: number;
  iterations_size: number;
  mutation_size: number;

  constructor(
    GD: number,
    population_size: number,
    iterations_size: number,
    mutation_size: number
  ) {
    this.GD = GD;
    this.population_size = population_size;
    this.iterations_size = iterations_size;
    this.mutation_size = mutation_size;
  }
}
