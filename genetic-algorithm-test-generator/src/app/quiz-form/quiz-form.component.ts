import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TestService } from '../services/test.service';
import { QuizConfig } from '../types/config';

@Component({
  selector: 'app-quiz-form',
  templateUrl: './quiz-form.component.html',
  styleUrls: ['./quiz-form.component.scss'],
})
export class QuizFormComponent implements OnInit {
  quizFormGroup: FormGroup;

  constructor(private testService: TestService, private fb: FormBuilder) {
    this.quizFormGroup = this.consturctorForm();
  }

  private consturctorForm = (): FormGroup => {
    return this.fb.group({
      GD: this.fb.control(10, [Validators.required]),
      population_size: this.fb.control(1000, [Validators.required]),
      iterations_size: this.fb.control(10000, [Validators.required]),
      mutation_size: this.fb.control(1000, [Validators.required]),
    });
  };

  ngOnInit(): void {}

  saveConfiguration() {
    if (!this.quizFormGroup) {
      return;
    }

    let body: any = {
      GD: this.quizFormGroup.get('GD')?.value.toString(),
      population_size: this.quizFormGroup
        .get('population_size')
        ?.value.toString(),
      iterations_size: this.quizFormGroup
        .get('iterations_size')
        ?.value.toString(),
      mutation_size: this.quizFormGroup.get('mutation_size')?.value.toString(),
    };

    let body2: FormData = new FormData();
    body2.append('GD', body.GD);
    body2.append('population_size', body.population_size);
    body2.append('iterations_size', body.iterations_size);
    body2.append('mutation_size', body.mutation_size);

    console.log(body2);
    this.testService.saveConfig(body2);
  }
}
