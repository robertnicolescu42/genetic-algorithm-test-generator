import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { TestService } from '../services/test.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
})
export class MainPageComponent implements OnInit {
  myResult: Observable<any>;

  constructor(private testService: TestService) {
    this.myResult = new Observable();
  }

  ngOnInit(): void {}

  getCall() {
    this.myResult = this.testService.getCall();

    this.myResult.subscribe((val) => console.log(val));
  }
}
