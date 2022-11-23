import { TestBed } from '@angular/core/testing';

import { PartidosService } from './partido.service';

describe('PartidoService', () => {
  let service: PartidosService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PartidosService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
