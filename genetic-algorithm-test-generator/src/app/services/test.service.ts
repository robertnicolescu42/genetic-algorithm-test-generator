import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { QuizConfig } from '../types/config';
import { map, catchError, tap } from 'rxjs/operators';

const httpHeaders = new HttpHeaders().set('content-type', 'application/json');

@Injectable({
  providedIn: 'root',
})
export class TestService {
  apiUrl: string = 'http://127.0.0.1:5000';
  constructor(private http: HttpClient) {}

  getCall(): Observable<any> {
    return this.http.get(this.apiUrl + '/questions');
  }

  saveConfig(config: any) {
    return this.http
      .put<any>(this.apiUrl + '/config', config, {
      })
      .pipe(
        map((item) => item),
        catchError((err) => {
          throw err;
        })
      ).subscribe();
  }
}
